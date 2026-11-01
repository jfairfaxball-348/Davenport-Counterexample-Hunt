"""S116 final ledger/pin checks; never invokes a target predicate."""
from pathlib import Path
import collections,hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'sessions/S116'
BASE='e541e5982fa972857f359838e25110db16e217b9'
sys.path.insert(0,str(ROOT/'tools/zsf'))
import pair_campaign


def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8')
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def old(p):return json.loads(git('show',BASE+':'+p))
def digest(data):return hashlib.sha256(data).hexdigest()
def normalized(p):
    data=(ROOT/p).read_bytes()
    return data if Path(p).suffix in ('.npy','.npz','.zip') else data.replace(b'\r\n',b'\n')


def main():
    claims=load('catalogue/claims.json')['claims'];sources=load('catalogue/sources.json')['sources']
    assert len(claims)==396 and claims[:394]==old('catalogue/claims.json')['claims']
    assert len(sources)==37 and sources==old('catalogue/sources.json')['sources']
    assert load('frontier/frontier.json')['rows']==old('frontier/frontier.json')['rows']
    for items,prefix in ((claims,'CLM'),(sources,'SRC')):
        assert [x['id'] for x in items]==[f'{prefix}-{i:04d}' for i in range(1,len(items)+1)]
    state=load('authoritative/STATE.json');before=old('authoritative/STATE.json')
    assert state['last_completed_session']=='S116' and state['recommended_next_session']=='S117'
    assert state['campaign_active'] is None and state['campaigns_preregistered']==['CAM-0008']
    for field in ['number_of_active_search_sessions','number_of_completed_materially_distinct_bounded_rounds','active_search_sessions','rounds','campaigns_completed','number_of_fallback_sessions']:
        assert state['counterexample_hunt_strategy'][field]==before['counterexample_hunt_strategy'][field]
    changed=set(git('diff','--name-only',BASE).splitlines())|set(git('ls-files','--others','--exclude-standard').splitlines())
    assert all(p=='campaigns/REGISTRY.md' or p.startswith('campaigns/CAM-0008/') for p in changed if p.startswith('campaigns/'))
    assert not any(p.startswith(('sessions/S115/','candidates/')) for p in changed)
    for mf in ['RUN_MANIFEST_V1.json','INTEGRATION_MANIFEST_V2.json']:
        for p,h in load('sessions/S116/'+mf)['code_sha256'].items():assert digest(normalized(p))==h,(mf,p)
    revision={'tools/zsf/pair_campaign.py':'sessions/S116/revisions/pair_campaign_v1.py','sessions/S116/integration.py':'sessions/S116/revisions/integration_v1.py'}
    for p,h in load('sessions/S116/INTEGRATION_MANIFEST.json')['code_sha256'].items():
        assert digest(normalized(revision.get(p,p)))==h,p
    for p,h in load('sessions/S116/INPUT_MANIFEST.json')['files'].items():assert digest((S/p).read_bytes())==h
    assert (S/'ENTRY_PROMPT.md').read_bytes()==subprocess.check_output(['git','show',BASE+':authoritative/NEXT_SESSION_PROMPT.md'],cwd=ROOT)
    spec=load('campaigns/CAM-0008/PREREGISTRATION.json')
    arrays=pair_campaign.prepare(spec)  # only loads/verifies inputs, never joins them
    assert list(map(len,arrays))==[145,40110] and spec['total']==5815950
    assert spec['candidate_directory']=='candidates/CAM-0008'
    assert len(spec['shards'])==145 and spec['chunk']==256
    assert spec['target_pairs_executed_at_registration']==0 and spec['max_parallel_jobs']==1
    assert set(spec['code_sha256'])=={'tools/zsf/pair_a.py','tools/zsf/pair_b.py','tools/zsf/pair_jobs.py','tools/zsf/pair_campaign.py'}
    pre=load('sessions/S116/PREFLIGHT.json');bench=load('sessions/S116/BENCHMARK.json');integration=load('sessions/S116/INTEGRATION.json')
    assert pre['status']==bench['status']==integration['status']=='PASS'
    assert sum(c['pairs'] for c in pre['cases'])==2400
    assert sum(c['counts'].get('ZERO',0)+c['counts'].get('ZSF',0) for c in pre['cases'])==1560
    assert integration['full_audit']['pairs']==600 and integration['full_audit']['every_zero_witness_checked']
    assert bench['target_pairs_evaluated']==integration['target_pairs_evaluated']==0
    assert sum(bench['tenfold_scenario_hours'].values())<36
    links=0
    for p in changed:
        if p.endswith('.json'):load(p)
        if p.endswith('.md') and (p.startswith(('sessions/S116/','campaigns/CAM-0008/')) or p in ['README.md','authoritative/START_HERE.md','authoritative/NEXT_SESSION_PROMPT.md','research/S116_PAIR_ENGINE_TOOLING.md']):
            for target in re.findall(r'\]\(([^)]+)\)',(ROOT/p).read_text(encoding='utf-8-sig')):
                if '://' not in target and not target.startswith('#'):
                    assert ((ROOT/p).parent/target.split('#')[0]).exists(),(p,target)
                    links+=1
    subprocess.run(['git','diff',BASE,'--check'],cwd=ROOT,check=True)
    exclude={'sessions/S116/VALIDATION.json','sessions/S116/SHA256SUMS.json'}
    hashes={p:digest(normalized(p)) for p in sorted(changed) if (ROOT/p).is_file() and p not in exclude}
    manifest={'algorithm':'SHA256, text normalized LF, binary raw','files':hashes,'excluded_self_and_validation':sorted(exclude)}
    (S/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
    result={'status':'PASS','claims_total':396,'claim_statuses':dict(collections.Counter(x['status'] for x in claims)),
            'old_claims_preserved':394,'sources_preserved':37,'frontier_rows_preserved':30,'historical_search_counters_preserved':True,
            'frozen_code_and_input_hashes':True,'old_integration_versions_preserved':True,'campaign_pins_checked_without_joining':True,
            'campaign':'CAM-0008 PREREGISTERED ONLY','settled_cases':2400,'legacy_cases':1560,'full_runtime_audit_cases':600,
            'target_pairs_evaluated':0,'links_checked':links,'manifest_files':len(hashes),'diff_check':'PASS','ci':'ABSENT_NOT_PASS','review':'INTERNAL_SAME_EXECUTOR'}
    (S/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
