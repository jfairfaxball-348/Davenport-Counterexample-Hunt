"""End-to-end settled runtime/audit validation, no target joins."""
from pathlib import Path
import hashlib,json,sys,tempfile,time
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/zsf'));sys.path.insert(0,str(Path(__file__).parent))
import pair_campaign as c
import pair_jobs as j
from preflight import spaces,key,rejected


def main():
    start=time.monotonic();results={}
    with tempfile.TemporaryDirectory(prefix='s116-integration-') as temp:
        root=Path(temp);refs=[]
        for p in (2,3):
            path=root/f'{p}.npy';np.save(path,np.array(spaces(p),dtype=np.uint64))
            refs.append({'path':str(path),'sha256':c.sha(path.read_bytes()),'count':{2:15,3:40}[p]})
        paths=['tools/zsf/pair_a.py','tools/zsf/pair_b.py','tools/zsf/pair_jobs.py','tools/zsf/pair_campaign.py']
        spec={'status':'PREREGISTERED','environment':c.environment(),'code_sha256':{p:c.sha((ROOT/p).read_bytes().replace(b'\r\n',b'\n')) for p in paths},
              'inputs':refs,'p':2,'q':3,'profile':[4]*4,'shards':[[0,201],[201,403],[403,600]],'total':600,'chunk':37,'absolute_run_cap_seconds':300}
        for engine in ('a','b'):
            for shard in range(3):
                receipt=c.run_spec(spec,engine,shard,root/'output'/engine/f'{shard:04d}',120)
                assert receipt['status']=='COMPLETE'
        summary=c.audit(spec,root/'output')
        assert summary['pairs']==600 and summary['counts']=={'ZERO':390,'INVALID':210}
        results['full_audit']=summary
        for field in ('environment','code_sha256','inputs','shards','total'):
            bad=json.loads(json.dumps(spec))
            if field=='environment':bad[field]['python']='wrong'
            elif field=='code_sha256':bad[field][paths[0]]='0'*64
            elif field=='inputs':bad[field][0]['sha256']='0'*64
            elif field=='shards':bad[field][1][0]=200
            else:bad[field]=601
            rejected(lambda:c.prepare(bad))
        results['spec_corruption_rejected']=['environment','code','input','shard overlap','total']
        # Rewriting a valid hash chain must not bypass the independent mathematical audit.
        folder=root/'output'/'b'/'0000'
        marker=folder/'000000000000.commit.json';rows=folder/'000000000000.rows.json'
        original=rows.read_bytes();markers={p:p.read_bytes() for p in folder.glob('*.commit.json')}
        def rechain():
            prev=c.sha(j.encoded(c.identity(spec,'b',0)))
            for path in sorted(markers):
                value=json.loads(path.read_bytes());value['previous']=prev
                value['output_sha256']=c.sha((folder/f"{value['start']:012d}.rows.json").read_bytes())
                raw=j.encoded(value);path.write_bytes(raw);prev=c.sha(raw)
        block=json.loads(original);block[0]['result']={'kind':'ZERO','witness':[0]*4};rows.write_bytes(j.encoded(block));rechain()
        rejected(lambda:c.audit(spec,root/'output'))
        for path,raw in markers.items():path.write_bytes(raw)
        rows.write_bytes(original)
        # An agreed wrong ZERO witness is independently rejected, not merely compared.
        afolder=root/'output'/'a'/'0000';apath=afolder/'000000000037.rows.json';ab=apath.read_bytes();bsecond=folder/'000000000037.rows.json';braw=bsecond.read_bytes();ams={p:p.read_bytes() for p in afolder.glob('*.commit.json')}
        for eng,fo in [('a',afolder),('b',folder)]:
            block=json.loads((fo/'000000000037.rows.json').read_bytes())
            idx=next(i for i,r in enumerate(block) if r['result']['kind']=='ZERO')
            block[idx]['result']['witness']=[0]*4
            (fo/'000000000037.rows.json').write_bytes(j.encoded(block))
            prev=c.sha(j.encoded(c.identity(spec,eng,0)))
            for path in sorted(fo.glob('*.commit.json')):
                value=json.loads(path.read_bytes());value['previous']=prev;value['output_sha256']=c.sha((fo/f"{value['start']:012d}.rows.json").read_bytes())
                raw=j.encoded(value);path.write_bytes(raw);prev=c.sha(raw)
        rejected(lambda:c.audit(spec,root/'output'))
        apath.write_bytes(ab);rows.write_bytes(original);bsecond.write_bytes(braw)
        for path,raw in {**markers,**ams}.items():path.write_bytes(raw)
        last=root/'output'/'b'/'0002'/'000000000588.commit.json'
        assert last.exists();raw=last.read_bytes();last.unlink()
        rejected(lambda:c.audit(spec,root/'output'));last.write_bytes(raw)
        assert c.audit(spec,root/'output')==summary
        results['audit_rejects']=['semantic disagreement with valid hashes','agreed zero witness corruption with valid hashes','partial coverage']
        # Single positive basis fixture for canonical preliminary export.
        positive=json.loads(json.dumps(spec));positive['inputs']=[]
        for p in (2,3):
            path=root/f'positive{p}.npy';np.save(path,np.array([key(np.eye(3,dtype=int),p)],dtype=np.uint64))
            positive['inputs'].append({'path':str(path),'sha256':c.sha(path.read_bytes()),'count':1})
        positive.update(profile=[5]*3,shards=[[0,1]],total=1,candidate_directory=str(root/'candidate-fixtures'))
        for engine in ('a','b'):
            dest=root/'positive'/engine
            receipt=c.run_spec(positive,engine,0,dest,120);assert receipt['status']=='CANDIDATE'
            candidate=json.loads((root/'candidate-fixtures'/f'{engine}-0000-000000000000.json').read_bytes())
            assert candidate['sequence_sha256']==c.sha(j.encoded(candidate['sequence'])) and len(candidate['sequence'])==15
            assert candidate['sequence']==sorted(candidate['sequence'])
        results['candidate_export']='two settled basis positives, canonical hash verified; not target candidates'
    results.update(status='PASS',seconds=time.monotonic()-start,target_pairs_evaluated=0)
    (ROOT/'sessions/S116/INTEGRATION.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(results,indent=2))


if __name__=='__main__':main()
