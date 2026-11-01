"""Hash-bound output-first chunk protocol. No mathematical predicate imports.

Filesystem durability is process-crash recovery, not a guarantee against power loss.
Committed corruption fails closed. Do not run concurrent writers for one shard.
"""
import hashlib
import json
import os
from pathlib import Path
import time


def encoded(value):return (json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()
def digest(data):return hashlib.sha256(data).hexdigest()


def atomic(path,data):
    temp=path.with_suffix(path.suffix+'.tmp')
    with temp.open('wb') as f:
        f.write(data);f.flush();os.fsync(f.fileno())
    os.replace(temp,path)


def inspect(folder,identity):
    folder=Path(folder);fingerprint=digest(encoded(identity))
    saved=json.loads((folder/'identity.json').read_bytes())
    if saved!=identity:raise ValueError('identity mismatch')
    cursor=identity['start'];chain=fingerprint;counts={};terminal=None;record_hash=hashlib.sha256()
    markers=sorted(folder.glob('*.commit.json'))
    for marker in markers:
        if terminal:raise ValueError('records after terminal')
        receipt=json.loads(marker.read_bytes())
        if marker.name!=f'{cursor:012d}.commit.json':raise ValueError('gap or duplicate')
        if receipt['start']!=cursor or receipt['previous']!=chain:raise ValueError('broken chain')
        data=(folder/f'{cursor:012d}.rows.json').read_bytes()
        if digest(data)!=receipt['output_sha256']:raise ValueError('corrupt output')
        block=json.loads(data)
        if not block or len(block)>identity['chunk']:raise ValueError('chunk size')
        for record in block:
            if terminal or record['ordinal']!=cursor:raise ValueError('bad ordinal or terminal')
            kind=record['result']['kind']
            if kind not in ('ZERO','INVALID','ZSF','FAILED'):raise ValueError('unknown outcome')
            if kind=='ZSF':terminal='CANDIDATE'
            if kind=='FAILED':terminal='FAILED'
            counts[kind]=counts.get(kind,0)+1;record_hash.update(encoded(record));cursor+=1
        if cursor!=receipt['stop'] or cursor>identity['stop']:raise ValueError('bad endpoint')
        chain=digest(encoded(receipt))
    return {'next':cursor,'chain':chain,'counts':counts,'record_sha256':record_hash.hexdigest(),'status':terminal or ('COMPLETE' if cursor==identity['stop'] else 'PARTIAL')}


def run(folder,identity,evaluate,budget_seconds,fault=None,max_chunks=None):
    if not 0<=identity['start']<=identity['stop'] or identity['chunk']<=0:raise ValueError('bad identity')
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    ip=folder/'identity.json'
    if not ip.exists():
        if list(folder.glob('*.commit.json')):raise ValueError('missing identity')
        atomic(ip,encoded(identity))
    state=inspect(folder,identity)
    if state['status']!='PARTIAL':return state
    began=time.monotonic();chunks=0
    while state['next']<identity['stop']:
        if time.monotonic()-began>=budget_seconds or (max_chunks is not None and chunks>=max_chunks):
            state=inspect(folder,identity);state['status']='BUDGET_EXHAUSTED';return state
        start=state['next'];stop=min(start+identity['chunk'],identity['stop']);block=[]
        try:
            for ordinal,result in evaluate(start,stop):
                if ordinal!=start+len(block) or ordinal>=stop:raise ValueError('enumeration coverage')
                if result.get('kind') not in ('ZERO','INVALID','ZSF'):raise ValueError('checker outcome')
                block.append({'ordinal':ordinal,'result':result})
                if result['kind']=='ZSF':break
            if len(block)!=stop-start and (not block or block[-1]['result']['kind']!='ZSF'):
                raise ValueError('truncated enumeration')
        except Exception as exc:
            # Discard every uncommitted decision in this chunk on any failure.
            block=[{'ordinal':start,'result':{'kind':'FAILED','error':type(exc).__name__+': '+str(exc)}}]
        if fault=='before_output':raise RuntimeError('injected before output')
        data=encoded(block);atomic(folder/f'{start:012d}.rows.json',data)
        if fault=='after_output':raise RuntimeError('injected after output')
        receipt={'start':start,'stop':start+len(block),'previous':state['chain'],'output_sha256':digest(data)}
        atomic(folder/f'{start:012d}.commit.json',encoded(receipt))
        if fault=='after_marker':raise RuntimeError('injected after marker')
        state['next']=receipt['stop'];state['chain']=digest(encoded(receipt));chunks+=1
        if block[-1]['result']['kind'] in ('ZSF','FAILED'):return inspect(folder,identity)
    return inspect(folder,identity)
