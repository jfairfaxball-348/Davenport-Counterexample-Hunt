"""Pinned pair-campaign entrypoint and independent record audit.

Only invoke against a registered campaign after its tooling gate is committed.
The generic entrypoint is exercised on settled fixtures by S116 integration tests.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import platform
import sys
import zipfile
import numpy as np
import pair_a
import pair_b
import pair_jobs

ROOT=Path(__file__).resolve().parents[2]


def sha(data):return hashlib.sha256(data).hexdigest()
def environment():return {'python':platform.python_version(),'platform':platform.platform(),'numpy':np.__version__}


def load_input(ref):
    if 'archive' in ref:
        archive=(ROOT/ref['archive']).read_bytes()
        if sha(archive)!=ref['archive_sha256']:raise ValueError('archive hash')
        with zipfile.ZipFile(io.BytesIO(archive)) as z:raw=z.read(ref['member'])
    else:raw=(ROOT/ref['path']).read_bytes()
    if sha(raw)!=ref['sha256']:raise ValueError('input hash')
    array=np.load(io.BytesIO(raw),allow_pickle=False)
    if array.ndim!=1 or array.dtype.kind!='u' or len(array)!=ref['count'] or not np.all(array[1:]>array[:-1]):
        raise ValueError('input format/order/count')
    return array


def prepare(spec):
    if spec['status']!='PREREGISTERED':raise ValueError('unregistered specification')
    if environment()!=spec['environment']:raise ValueError('environment mismatch')
    for path,expected in spec['code_sha256'].items():
        if sha((ROOT/path).read_bytes().replace(b'\r\n',b'\n'))!=expected:raise ValueError('code mismatch: '+path)
    first,second=load_input(spec['inputs'][0]),load_input(spec['inputs'][1])
    total=len(first)*len(second)
    cursor=0
    for lo,hi in spec['shards']:
        if lo!=cursor or not lo<hi<=total:raise ValueError('shard partition')
        cursor=hi
    if cursor!=total or total!=spec['total']:raise ValueError('total coverage')
    return first,second


def identity(spec,engine,shard):
    lo,hi=spec['shards'][shard]
    return {'spec_sha256':sha(pair_jobs.encoded(spec)),'engine':engine,'start':lo,'stop':hi,'chunk':spec['chunk'],
            'profile':spec['profile'],'code':spec['code_sha256'],'environment':spec['environment'],
            'inputs':spec['inputs']}


def run_spec(spec,engine,shard,folder,seconds):
    if engine not in ('a','b') or not 0<=shard<len(spec['shards']):raise ValueError('job selector')
    if not 0<=seconds<=spec['absolute_run_cap_seconds']:raise ValueError('run budget')
    first,second=prepare(spec);module=pair_a if engine=='a' else pair_b
    evaluate=lambda lo,hi:module.traverse(first,second,lo,hi,spec['p'],spec['q'],spec['profile'])
    result=pair_jobs.run(folder,identity(spec,engine,shard),evaluate,seconds)
    if result['status']=='CANDIDATE':
        ordinal=result['next']-1;i,j=divmod(ordinal,len(second))
        matrix=pair_a.actual(first[i],second[j],spec['p'],spec['q'],len(spec['profile']))
        sequence=sorted([list(map(int,matrix[:,col])) for col,t in enumerate(spec['profile']) for _ in range(t)])
        encoded=pair_jobs.encoded(sequence)
        candidate={'status':'UNVERIFIED_CANDIDATE','ordinal':ordinal,'sequence':sequence,'sequence_sha256':sha(encoded),
                   'spec_sha256':sha(pair_jobs.encoded(spec)),'engine':engine,
                   'required':'Independent checking, Lean kernel verification and later-session cold check before certification.'}
        destination=ROOT/spec['candidate_directory']
        destination.mkdir(parents=True,exist_ok=True)
        pair_jobs.atomic(destination/f'{engine}-{shard:04d}-{ordinal:012d}.json',pair_jobs.encoded(candidate))
    pair_jobs.atomic(Path(folder)/'RESULT.json',pair_jobs.encoded(result))
    return result


def audit(spec,output):
    """Independent interval/record traversal; directly checks every emitted zero.

    Does not rely on runner summary or runner inspect implementation.
    Full semantic A/B agreement is necessary in addition to matching totals.
    """
    first,second=prepare(spec);output=Path(output);n=spec['p']*spec['q'];alpha=spec['profile']
    counts={'ZERO':0,'INVALID':0};total=0
    for shard,(lo,hi) in enumerate(spec['shards']):
        def records(engine):
            folder=output/engine/f'{shard:04d}'
            expected=identity(spec,engine,shard)
            if json.loads((folder/'identity.json').read_bytes())!=expected:raise ValueError('audit identity')
            prev=sha(pair_jobs.encoded(expected));cursor=lo
            for path in sorted(folder.glob('*.commit.json')):
                marker=json.loads(path.read_bytes())
                if path.name!=f'{cursor:012d}.commit.json' or marker['start']!=cursor or marker['previous']!=prev:raise ValueError('audit chain/gap')
                raw=(folder/f'{cursor:012d}.rows.json').read_bytes()
                if sha(raw)!=marker['output_sha256']:raise ValueError('audit output hash')
                block=json.loads(raw)
                if not 0<len(block)<=spec['chunk']:raise ValueError('audit chunk size')
                for record in block:
                    if record['ordinal']!=cursor or cursor>=hi:raise ValueError('audit ordinal')
                    cursor+=1;yield record
                if cursor!=marker['stop']:raise ValueError('audit endpoint')
                prev=sha(pair_jobs.encoded(marker))
            if cursor!=hi:raise ValueError('incomplete shard')
        ra,rb=records('a'),records('b')
        for ordinal in range(lo,hi):
            aa,bb=next(ra,None),next(rb,None)
            if aa is None or bb is None or aa['ordinal']!=ordinal or bb['ordinal']!=ordinal:raise ValueError('missing record')
            kind=aa['result']['kind']
            if kind not in counts or bb['result']['kind']!=kind:raise ValueError('candidate/failure/disagreement')
            row,col=divmod(ordinal,len(second));k=len(alpha)
            # Third CRT reconstruction: search each residue, not either engine decoder.
            m=[[next(t for t in range(n) if t%spec['p']==(int(first[row])//spec['p']**(r*k+c))%spec['p'] and t%spec['q']==(int(second[col])//spec['q']**(r*k+c))%spec['q']) for c in range(k)] for r in range(3)]
            columns=list(zip(*m));valid=len(set(columns))==k and all(next(t for t in range(1,n+1) if all(t*x%n==0 for x in g))==n for g in columns)
            if kind=='INVALID' and valid:raise ValueError('false inadmissibility')
            if kind=='ZERO':
                if not valid:raise ValueError('unfiltered invalid support')
                for result in (aa['result'],bb['result']):
                    w=result['witness']
                    if len(w)!=k or not any(w) or not all(type(x) is int and 0<=x<=bound for x,bound in zip(w,alpha)) or any(sum(x*y for x,y in zip(mr,w))%n for mr in m):raise ValueError('audit invalid witness')
            counts[kind]+=1;total+=1
        if next(ra,None) is not None or next(rb,None) is not None:raise ValueError('extra record')
    if total!=spec['total']:raise ValueError('audit total')
    return {'status':'COMPLETE_TWO_ENGINE_AGREEMENT','pairs':total,'counts':counts,'every_zero_witness_checked':True,'spec_sha256':sha(pair_jobs.encoded(spec))}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('spec');parser.add_argument('output')
    parser.add_argument('--engine',choices=['a','b']);parser.add_argument('--shard',type=int);parser.add_argument('--seconds',type=float,default=21600)
    parser.add_argument('--audit',action='store_true');args=parser.parse_args()
    spec=json.loads(Path(args.spec).read_text(encoding='utf-8'))
    if args.audit:result=audit(spec,args.output)
    else:
        if args.engine is None or args.shard is None:parser.error('engine and shard required')
        result=run_spec(spec,args.engine,args.shard,Path(args.output)/args.engine/f'{args.shard:04d}',args.seconds)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
