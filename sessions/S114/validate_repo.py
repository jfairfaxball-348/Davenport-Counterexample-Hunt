"""S114 consistency checks; no research search. Run from repository root."""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = 'e2689ba76c775b7559a3073f979d62f1b8a148f2'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8')


def read(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8-sig'))


def old(path):
    return json.loads(git('show', BASE+':'+path))


def evidence_bytes(path):
    data = (ROOT/path).read_bytes()
    if path not in {'sessions/S114/ENTRY_PROMPT.md','sessions/S114/INPUT.md','sessions/S114/PLAN.md'}:
        data = data.replace(b'\r\n', b'\n')
    return data


def main():
    claims = read('catalogue/claims.json')['claims']
    sources = read('catalogue/sources.json')['sources']
    assert claims[:383] == old('catalogue/claims.json')['claims']
    assert len(claims) == 390 and len(sources) == 37
    for records, prefix in [(claims, 'CLM'), (sources, 'SRC')]:
        assert [c['id'] for c in records] == [f'{prefix}-{i:04d}' for i in range(1,len(records)+1)]
    assert read('frontier/frontier.json')['rows'] == old('frontier/frontier.json')['rows']
    original_sources = old('catalogue/sources.json')['sources']
    assert original_sources == read('sessions/S114/SOURCE_RECORDS_AT_ENTRY.json')['sources']
    promoted = {'SRC-0029','SRC-0031','SRC-0032'}
    for before, after in zip(original_sources,sources):
        if before['id'] not in promoted:
            assert before == after
        else:
            assert after['access_history'][-1] == {k:before[k] for k in ['access','accessed','notes']}
    state = read('authoritative/STATE.json')
    prior = old('authoritative/STATE.json')
    assert state['last_completed_session'] == 'S114' and state['recommended_next_session'] == 'S115'
    assert state['campaign_active'] is None and state['campaigns_preregistered'] == []
    for key in ['number_of_active_search_sessions','number_of_completed_materially_distinct_bounded_rounds',
                'active_search_sessions','rounds','campaigns_completed','number_of_fallback_sessions']:
        assert state['counterexample_hunt_strategy'][key] == prior['counterexample_hunt_strategy'][key]
    changed = set(git('diff','--name-only',BASE).splitlines())
    changed.update(git('ls-files','--others','--exclude-standard').splitlines())
    assert all(p == 'campaigns/REGISTRY.md' for p in changed if p.startswith('campaigns/'))
    source_ids = {s['id'] for s in sources}
    for c in claims:
        assert set(c.get('source_ids',[])) <= source_ids
    for p,h in read('sessions/S114/RESULTS.json')['code_sha256'].items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == h
    for p,h in read('sessions/S114/INPUT_MANIFEST.json')['files'].items():
        assert hashlib.sha256((ROOT/'sessions/S114'/p).read_bytes()).hexdigest() == h
    for p in changed:
        if p.endswith('.json'):
            read(p)
    # Check new/live documents; historical markdown retains historical link syntax.
    links_checked = 0
    for p in ['README.md','authoritative/START_HERE.md','authoritative/NEXT_SESSION_PROMPT.md',
              'research/S114_IMAGE_FEASIBILITY.md', *[str(x.relative_to(ROOT)).replace('\\','/') for x in (ROOT/'sessions/S114').glob('*.md')]]:
        for target in re.findall(r'\]\(([^)]+)\)', (ROOT/p).read_text(encoding='utf-8-sig')):
            if '://' not in target and not target.startswith('#'):
                assert ((ROOT/p).parent/target.split('#')[0]).exists(), (p,target)
                links_checked += 1
    subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
    hashes = {p:hashlib.sha256(evidence_bytes(p)).hexdigest() for p in sorted(changed)
              if (ROOT/p).is_file() and p not in ['sessions/S114/SHA256SUMS.json','sessions/S114/VALIDATION.json']}
    manifest = {'algorithm':'SHA-256 LF-normalized text; ENTRY_PROMPT/INPUT/PLAN use raw archived bytes (Git -text)', 'files':hashes,
                'excludes':['sessions/S114/SHA256SUMS.json','sessions/S114/VALIDATION.json']}
    (ROOT/'sessions/S114/SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    for p,h in read('sessions/S114/SHA256SUMS.json')['files'].items():
        assert hashlib.sha256(evidence_bytes(p)).hexdigest() == h
    result = {'status':'PASS','entry_main':BASE,'historical_claims_unchanged':383,'frontier_rows_unchanged':30,
              'claims':len(claims),'sources':len(sources),'claim_statuses':dict(collections.Counter(c['status'] for c in claims)),
              'source_access':dict(collections.Counter(s['access'] for s in sources)),
              'old_campaign_artifacts_unchanged':True,'search_counters_unchanged':True,'source_histories_verified':True,
              'new_local_links_checked':links_checked,'manifest_files_verified':len(hashes),
              'input_and_research_code_hashes_verified':True,'git_diff_check':'PASS','ci':'ABSENT_NOT_PASS',
              'review':'INTERNAL_SAME_EXECUTOR'}
    (ROOT/'sessions/S114/VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
