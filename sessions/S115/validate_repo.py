"""Read-only research/ledger verification plus final normalized evidence manifest."""
import collections
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
BASE='3039bcaa52238bb21c2127ddb1c66c54f153c89b'
S=ROOT/'sessions/S115'


def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8')
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def old(p):return json.loads(git('show',BASE+':'+p))
def digest(data):return hashlib.sha256(data).hexdigest()
def normalized(p):
    data=(ROOT/p).read_bytes()
    return data if Path(p).suffix in {'.zip','.npz','.npy'} else data.replace(b'\r\n',b'\n')


def main():
    claims=load('catalogue/claims.json')['claims'];sources=load('catalogue/sources.json')['sources']
    assert len(claims)==394 and claims[:390]==old('catalogue/claims.json')['claims']
    assert sources==old('catalogue/sources.json')['sources'] and len(sources)==37
    assert load('frontier/frontier.json')['rows']==old('frontier/frontier.json')['rows']
    for items,prefix in [(claims,'CLM'),(sources,'SRC')]:
        assert [x['id'] for x in items]==[f'{prefix}-{i:04d}' for i in range(1,len(items)+1)]
    state=load('authoritative/STATE.json');before=old('authoritative/STATE.json')
    assert state['last_completed_session']=='S115' and state['recommended_next_session']=='S116'
    assert state['campaign_active'] is None and not state['campaigns_preregistered']
    for k in ['number_of_active_search_sessions','number_of_completed_materially_distinct_bounded_rounds','active_search_sessions','rounds','campaigns_completed','number_of_fallback_sessions']:
        assert state['counterexample_hunt_strategy'][k]==before['counterexample_hunt_strategy'][k]
    changed=set(git('diff','--name-only',BASE).splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
    assert all(p=='campaigns/REGISTRY.md' for p in changed if p.startswith('campaigns/'))
    assert not any(p.startswith(('sessions/S114/','candidates/')) for p in changed)
    archive=load('sessions/S115/ARCHIVE_MANIFEST.json')
    assert digest((S/'LOCAL_EVIDENCE.zip').read_bytes())==archive['sha256']
    with zipfile.ZipFile(S/'LOCAL_EVIDENCE.zip') as z:
        assert set(z.namelist())==set(archive['files'])
        for name,h in archive['files'].items():assert digest(z.read(name))==h,name
        def artifact(path):
            local=ROOT/path
            return local.read_bytes() if local.exists() else z.read(str(Path(path).relative_to('sessions/S115')).replace('\\','/'))
        for mf,field in [('RUN_MANIFEST.json','code_sha256'),('ORBIT_RUN_MANIFEST.json','sha256'),('THEORY_RUN_MANIFEST.json','code_sha256')]:
            for p,h in load('sessions/S115/'+mf)[field].items():
                data=artifact(p)
                if Path(p).suffix not in {'.npy','.npz','.zip'}:data=data.replace(b'\r\n',b'\n')
                assert digest(data)==h,(mf,p)
        for p,h in load('sessions/S115/INPUT_MANIFEST.json')['files'].items():
            assert digest((S/p).read_bytes())==h,p
        results=load('sessions/S115/RESULTS.json')
        for p in (3,5):
            for key in ['all']+[f'profile{i}' for i in range(5)]:
                aa=np.load(io.BytesIO(z.read(f'data/a{p}/{key}.npy')),allow_pickle=False)
                bb=np.load(io.BytesIO(z.read(f'data/b{p}/{key}.npy')),allow_pickle=False)
                assert np.array_equal(aa,bb)
                assert len(aa)==len(np.unique(aa))
                if key=='all':assert len(aa)=={3:33880,5:2558556}[p]
                else:
                    i=int(key[-1]);r=results['components'][str(p)]
                    assert len(aa)==r['survivors'][i]
                    assert digest(aa.astype('<u8').tobytes())==r['survivor_key_sha256_le_uint64'][i]
        orbit=load('sessions/S115/ORBIT_RESULTS.json')
        for i,case in enumerate(orbit['cases']):
            reps=np.load(S/f'representatives{i}.npy',allow_pickle=False)
            assert len(reps)==case['p3_orbits']
            assert digest(reps.astype('<u8').tobytes())==case['representative_sha256_le_uint64']
            assert sum(int(k)*v for k,v in case['orbit_size_histogram'].items())==case['p3_survivors']
        assert sum(x['representative_product'] for x in orbit['cases'])==718716282
    for p in changed:
        if p.endswith('.json'):load(p)
    link_count=0
    for p in ['README.md','authoritative/START_HERE.md','authoritative/NEXT_SESSION_PROMPT.md','research/S115_LOCAL_KERNEL_PRUNING.md',*[str(x.relative_to(ROOT)).replace('\\','/') for x in S.glob('*.md')]]:
        for target in re.findall(r'\]\(([^)]+)\)',(ROOT/p).read_text(encoding='utf-8-sig')):
            if '://' not in target and not target.startswith('#'):
                assert ((ROOT/p).parent/target.split('#')[0]).exists(),(p,target)
                link_count+=1
    subprocess.run(['git','diff',BASE,'--check'],cwd=ROOT,check=True)
    excludes={'sessions/S115/SHA256SUMS.json','sessions/S115/VALIDATION.json'}
    hashes={p:digest(normalized(p)) for p in sorted(changed) if (ROOT/p).is_file() and p not in excludes}
    manifest={'algorithm':'SHA256; binary zip/npy/npz raw, other text CRLF normalized to LF','files':hashes,'excludes':sorted(excludes)}
    (S/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    out={'status':'PASS','historical_claims_unchanged':390,'source_objects_unchanged':37,'frontier_rows_unchanged':30,
         'claims_total':394,'claim_statuses':dict(collections.Counter(c['status'] for c in claims)),
         'archived_files_byte_verified':len(archive['files']),'full_local_sets_equal':True,'orbit_evidence_verified':True,
         'frozen_inputs_code_manifests_verified':True,'search_counters_and_campaign_artifacts_unchanged':True,
         'new_local_links_checked':link_count,'manifest_files':len(hashes),'diff_check':'PASS','ci':'ABSENT_NOT_PASS','review':'INTERNAL_SAME_EXECUTOR'}
    (S/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
