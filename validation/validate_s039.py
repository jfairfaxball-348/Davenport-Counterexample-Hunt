#!/usr/bin/env python3
"""S039 repository integrity; no mathematical instance computation or search."""
import hashlib,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
checks={}
def check(n,v):
 checks[n]=bool(v)
 if not v: raise AssertionError(n)
def read(p):return json.loads((R/p).read_text())
def old(p):return subprocess.check_output(['git','show',ENTRY+':'+p],cwd=R)
def git(*a):return subprocess.check_output(['git',*a],cwd=R,text=True).strip()
ENTRY='99018af95fe5dd35a915cf5171a40aa0bc86a5e0'
for p in R.rglob('*.json'):
 if '.git' not in p.parts:json.loads(p.read_text())
check('all_json_parses',True)
c=read('catalogue/claims.json');s=read('catalogue/sources.json');f=read('frontier/frontier.json');st=read('authoritative/STATE.json');v=read('sessions/S039/VALIDATION.json');e=read('sessions/S039/ENTRY_REVIEW.json')
check('old141_claim_objects_preserved',c['claims'][:141]==json.loads(old('catalogue/claims.json'))['claims'])
check('147_unique_claim_ids',[x['id'] for x in c['claims']]==[f'CLM-{i:04d}' for i in range(1,148)])
check('original28_source_objects_preserved',s['sources']==json.loads(old('catalogue/sources.json'))['sources'])
check('source_enums_preserved',s['access_enum']==json.loads(old('catalogue/sources.json'))['access_enum'])
check('claim_enums_preserved',c['status_enum']==json.loads(old('catalogue/claims.json'))['status_enum'])
check('original30_frontier_objects_preserved',f['rows']==json.loads(old('frontier/frontier.json'))['rows'])
check('source_ids_unique',[x['id'] for x in s['sources']]==[f'SRC-{i:04d}' for i in range(1,29)])
ids={x['id'] for x in c['claims']};src={x['id'] for x in s['sources']}
check('valid_source_refs',all(set(x.get('source_ids',[]))<=src for x in c['claims']))
check('valid_statuses',all(x['status'] in c['status_enum'] for x in c['claims']) and all(x['access'] in s['access_enum'] for x in s['sources']))
check('all_new_claims_programme_proved',all(x['status']=='PROGRAMME_PROVED' for x in c['claims'][141:]))
check('new_origins_exist',all((R/x['origin']).is_file() for x in c['claims'][141:]))
check('old_catalogue_markdown_prefixes_preserved',all((R/p).read_bytes().startswith(old(p).rstrip()) for p in ['catalogue/CLAIMS.md','catalogue/SOURCES.md']))
check('new_claim_markdown_mirrors',all(x['statement'] in (R/'catalogue/CLAIMS.md').read_text() and '## '+x['id']+' — ' in (R/'catalogue/CLAIMS.md').read_text() for x in c['claims'][141:]))
check('no_computed_or_formal_promotions',not any(x['status'] in ['COMPUTED_EXACT','FORMALLY_CERTIFIED'] for x in c['claims']))
pat=re.compile(r'^\| \d+ \|',re.M)
rows=lambda txt:[line for line in txt.splitlines() if pat.match(line)]
md=(R/'frontier/FRONTIER.md').read_text()
check('30_exact_full_ordered_markdown_rows_preserved',rows(md)==rows(old('frontier/FRONTIER.md').decode()) and len(rows(md))==30)
for row,line in zip(f['rows'],rows(md)):
 cols=[x.strip() for x in line.split('|')][1:-1]
 check('row_'+str(row['n'])+'_entire_mirror',cols==[str(row['n']),row['group'],str(row['d_star']),row['reported_bound'],row['provisional_status'],', '.join(row['evidence'])])
check('five_frozen_intervals',[(r['n'],r['lower_bound'],r['upper_bound']) for r in f['rows'] if r['lower_bound']!=r['upper_bound']]==[(15,43,45),(20,58,59),(21,61,63),(28,82,83),(30,88,90)])
check('phases_preserved',st['phases']==json.loads(old('authoritative/STATE.json'))['phases'])
check('current_state_and_handoff',st['last_completed_session']=='S039' and st['recommended_next_session']=='S040' and st['phases']['1']['status']=='IN_PROGRESS')
check('no_campaign_or_candidate',st['campaign_active'] is None and st['counterexample_status']=='NONE_CLAIMED')
check('no_obsolete_current_D2_blocker',all('UNPROVED' not in x or 'D2' not in x for x in st['open_blockers']))
check('all_spine_records_synced',all('S039' in (R/p).read_text() for p in ['authoritative/START_HERE.md','authoritative/DECISION_LOG.md','docs/PHASE_GATE_LEDGER.md','docs/SESSION_LEDGER.md','docs/FAILURE_AND_LESSON_LEDGER.md','campaigns/REGISTRY.md','research/FOUNDATIONS.md','catalogue/CLAIMS.md','catalogue/SOURCES.md','frontier/FRONTIER.md']))
im=read('sessions/S039/INPUT_MANIFEST.json');ib=(R/'sessions/S039/INPUT.md').read_bytes()
check('canonical_input_byte_exact',ib==old('authoritative/NEXT_SESSION_PROMPT.md'))
check('canonical_git_blob_exact',git('hash-object','sessions/S039/INPUT.md')==im['canonical_git_blob_sha']==git('rev-parse',ENTRY+':authoritative/NEXT_SESSION_PROMPT.md'))
check('canonical_archive_digest_exact',hashlib.sha256(ib).hexdigest()==im['canonical_archive_sha256'])
check('no_fabricated_raw_chat_digest',im['raw_chat_sha256'] is None and not im['authenticated_raw_chat_bytes_available'])
check('separate_owner_invocation',(R/'sessions/S039/OWNER_INVOCATION.md').is_file() and (R/'sessions/S039/OWNER_INVOCATION.md').read_bytes()!=ib)
future=(R/'authoritative/NEXT_SESSION_PROMPT.md').read_bytes();fm=read('sessions/S039/FUTURE_HANDOFF_MANIFEST.json');close=(R/'sessions/S039/CLOSEOUT.md').read_bytes()
check('future_archived_exact',close.split(b'<!-- S040_PROMPT_START -->\n',1)[1].split(b'<!-- S040_PROMPT_END -->',1)[0]==future)
check('future_digest_and_length',hashlib.sha256(future).hexdigest()==fm['sha256'] and len(future)==fm['bytes'])
check('S040_unexecuted',b'FUTURE, UNEXECUTED' in future and not (R/'sessions/S040').exists() and not v['future_session_executed'])
check('prior_S038_one_atomic_commit',git('show','-s','--format=%P',e['prior_head'])==e['prior_head_parent'] and git('rev-list','--count',e['prior_head_parent']+'..'+e['prior_head'])=='1')
check('prior_merge_two_parent_tree',git('show','-s','--format=%P',e['prior_merge']).split()==e['prior_merge_parents'] and git('show','-s','--format=%T',e['prior_head'])==git('show','-s','--format=%T',e['prior_merge'])==e['prior_tree'])
check('intervening_only_prompt',git('diff','--name-only',e['prior_merge'],ENTRY)=='authoritative/NEXT_SESSION_PROMPT.md')
check('entry_exact_tree',git('show','-s','--format=%T',ENTRY)==e['entry_tree'])
check('hosted_absence_not_pass',e['workflow_runs']==e['check_runs']==e['status_contexts']==0 and e['hosted_ci']=='ABSENT_NOT_PASS' and not v['hosted_ci_pass'])
check('inaccessible_endpoints_unknown','UNKNOWN' in e['branch_protection'] and 'UNKNOWN' in e['workflow_listing_api'])
check('actual_workflow_files_absent',not any(p.startswith('.github/workflows/') for p in git('ls-tree','-r','--name-only',ENTRY).splitlines()))
check('all_four_fronts_and_synthesis',v['all_four_fronts_attempted'] and v['cross_front_synthesis'])
check('proof_scope_honest',v['D2_saving_proved'] and v['downstream_M_comparison_proved'] and not any(v[x] for x in ['strong_extraction_proved','general_eta_proved_here','m2p_excluded','higher_layers_excluded','composite_Davenport_conjecture_resolved','external_independent_review','formal_proof','novelty_claim','mathematical_instance_search','campaign_run']))
check('historical_bypass_acknowledged',v['historical_S004_bypass_acknowledged'] and 'CLM-0068' in (R/'sessions/S039/SUBPROBLEM_LEDGER.md').read_text())
for p in list((R/'sessions/S039').glob('*.md'))+list((R/'research').glob('S039*.md')):
 check(str(p.relative_to(R))+'_claim_refs',set(re.findall(r'\bCLM-\d{4}\b',p.read_text()))<=ids)
 check(str(p.relative_to(R))+'_source_refs',set(re.findall(r'\bSRC-\d{4}\b',p.read_text()))<=src)
changed=git('diff','--name-only',ENTRY).splitlines()
check('historical_session_records_untouched',not any(p.startswith('sessions/') and not p.startswith('sessions/S039/') for p in changed))
check('historical_research_records_untouched',not any(p.startswith('research/S0') and not p.startswith('research/S039') for p in changed))
result={'session':'S039','kind':'ADMINISTRATIVE_ONLY','result':'PASS','checks_passed':len(checks),'checks':checks,'mathematical_certification':False,'hosted_ci_pass':False,'mathematical_instance_search':False,'limitations':['Symbolic proof independently reconstructed by same executor, not verified by this program.','No formal or external certification.','No hosted CI pass.']}
(R/'validation/S039_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
print('S039 administrative PASS:',len(checks),'checks; not mathematical certification or hosted CI')
