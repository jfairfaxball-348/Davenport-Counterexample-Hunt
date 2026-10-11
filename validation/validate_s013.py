#!/usr/bin/env python3
"""S013 administrative consistency only: no mathematical computation or source execution."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks={}
def check(name,condition):
 checks[name]=bool(condition)
 if not condition:raise AssertionError(name)
def read(p):return json.loads((ROOT/p).read_text())
def main():
 files=[p for p in ROOT.rglob('*.json') if '.git' not in p.parts]
 for p in files:json.loads(p.read_text())
 check('all_repository_json_parses',True)
 s=read('catalogue/sources.json');c=read('catalogue/claims.json');f=read('frontier/frontier.json');st=read('authoritative/STATE.json');e=read('sessions/S013/ENTRY_REVIEW.json');v=read('validation/S013_REVIEW.json')
 si=[x['id'] for x in s['sources']];ci=[x['id'] for x in c['claims']]
 check('28_unique_stable_source_ids',si==[f'SRC-{i:04d}' for i in range(1,29)])
 check('93_unique_stable_claim_ids',ci==[f'CLM-{i:04d}' for i in range(1,94)])
 check('enums',all(x['access'] in s['access_enum'] for x in s['sources']) and all(x['status'] in c['status_enum'] for x in c['claims']))
 check('claim_source_refs',all(set(x.get('source_ids',[]))<=set(si) for x in c['claims']))
 check('inherited_quarantine',all(x['status']=='INHERITED_UNVERIFIED' for x in c['claims'][:37]))
 check('no_computed_or_formal_claim',not any(x['status'] in ['COMPUTED_EXACT','FORMALLY_CERTIFIED'] for x in c['claims']))
 base=e['entry_main']
 prev=json.loads(subprocess.check_output(['git','show',base+':catalogue/claims.json'],cwd=ROOT))
 check('all_88_previous_claims_preserved_byte_fields',c['claims'][:88]==prev['claims'])
 check('new_scoped_claims',all(x['status']=='PROGRAMME_PROVED' and x['origin'].startswith('research/S013_') for x in c['claims'][88:]))
 check('gg_full_claim_source_stated',c['claims'][81]['status']=='SOURCE_STATED' and not v['gg1999_full_chain_proved'])
 for file,items,key in [('catalogue/CLAIMS.md',c['claims'],'status'),('catalogue/SOURCES.md',s['sources'],'access')]:
  text=(ROOT/file).read_text()
  check(file+'_all_id_sections',all(len(re.findall(r'^## '+x['id']+r' — ',text,re.M))==1 for x in items))
  for x in items:
   section=text.split('## '+x['id']+' — ',1)[1].split('\n## ',1)[0]
   check(x['id']+'_md_status',x[key] in section)
 check('frontier_30_unique', [x['n'] for x in f['rows']]==list(range(1,31)))
 old=json.loads(subprocess.check_output(['git','show',base+':frontier/frontier.json'],cwd=ROOT))
 check('all_frontier_rows_unchanged',f['rows']==old['rows'])
 md=(ROOT/'frontier/FRONTIER.md').read_text()
 rows={int(cols[1]):cols[2:] for line in md.splitlines() if re.match(r'^\| \d+ \|',line) for cols in [[x.strip() for x in line.split('|')]]}
 check('frontier_md_30',len(rows)==30)
 for x in f['rows']:
  check('frontier_n'+str(x['n'])+'_mirror',rows[x['n']][:4]==[x['group'],str(x['d_star']),x['reported_bound'],x['provisional_status']] and rows[x['n']][4]==', '.join(x['evidence']))
 known=set(si+ci)
 check('frontier_refs',all(set(x['evidence']) <= known|{'TRIVIAL_GROUP'} for x in f['rows']))
 check('five_intervals',[(x['n'],x['lower_bound'],x['upper_bound']) for x in f['rows'] if x['lower_bound']!=x['upper_bound']]==[(15,43,45),(20,58,59),(21,61,63),(28,82,83),(30,88,90)])
 check('phase_statuses',st['last_completed_session']=='S013' and st['recommended_next_session']=='S014' and st['phases']['1']['status']=='IN_PROGRESS' and all(st['phases'][str(i)]['status']=='NOT_STARTED' for i in [2,3]))
 campaign=(ROOT/'campaigns/REGISTRY.md').read_text();check('campaign_blocked',st['campaign_active'] is None and all(x in campaign for x in ['S013','PROPOSED / NOT RUNNING','BLOCKED','16']))
 check('all_ledgers_synchronized',all('S013' in (ROOT/p).read_text() for p in ['authoritative/START_HERE.md','authoritative/DECISION_LOG.md','docs/PHASE_GATE_LEDGER.md','docs/SESSION_LEDGER.md','docs/FAILURE_AND_LESSON_LEDGER.md','research/FOUNDATIONS.md','catalogue/SOURCES.md','catalogue/CLAIMS.md']))
 inp=(ROOT/'sessions/S013/INPUT.md').read_bytes();im=read('sessions/S013/INPUT_MANIFEST.json')
 orig=subprocess.check_output(['git','show',base+':authoritative/NEXT_SESSION_PROMPT.md'],cwd=ROOT)
 check('input_committed_handoff_byte_exact',inp==orig and hashlib.sha256(inp).hexdigest()==im['committed_handoff_sha256'] and len(inp)==im['committed_handoff_bytes'])
 check('separate_invocation_no_transport_hash', (ROOT/'sessions/S013/OWNER_INVOCATION.md').exists() and 'transport bytes unavailable' in im['owner_invocation'])
 fut=(ROOT/'authoritative/NEXT_SESSION_PROMPT.md').read_bytes();cl=(ROOT/'sessions/S013/CLOSEOUT.md').read_bytes();fm=read('sessions/S013/FUTURE_HANDOFF_MANIFEST.json')
 embedded=cl.split(b'<!-- S014_PROMPT_START -->\n',1)[1].split(b'<!-- S014_PROMPT_END -->',1)[0]
 check('future_handoff_byte_identity',fut==embedded and len(fut)==fm['bytes'] and hashlib.sha256(fut).hexdigest()==fm['sha256'])
 check('future_unexecuted',b'FUTURE, UNEXECUTED' in fut and not v['future_session_executed'] and not (ROOT/'sessions/S014').exists())
 check('prior_atomic_merge_reconciled',e['prior_pr_commit_count']==1 and e['prior_merge_parents']==[e['prior_s012_head_parent'],e['prior_s012_head']] and e['prior_merge_tree']==e['prior_s012_head_tree']==e['entry_tree'] and e['git_ls_remote_independently_agrees'])
 check('no_hosted_ci_pass',not e['ci_pass_claimed'] and not v['hosted_ci_pass'] and e['hosted_action_runs']==e['check_runs']==e['status_contexts']==0)
 check('no_search_or_source_execution',not v['source_program_execution'] and v['mathematical_numerical_searches']==0 and not read('sessions/S013/SOURCE_MANIFEST.json')['author_code_executed'])
 check('no_unconditional_eta_or_coefficient',not v['rank_three_eta7_unconditional'] and not v['stronger_coefficient_proved'])
 check('no_copyrighted_primary_files_committed',not any(p.suffix in ['.pdf','.tex'] for p in ROOT.rglob('*') if '.git' not in p.parts))
 check('conditional_GG_and_rank_two_scope',v['rank_two_prerequisites_independently_proved'] and v['gg_B_implies_C_conditional_proved'] and v['original_lemma10_6_conditional_proved'] and not v['unconditional_property_B_proved'])
 check('original_Olson_body_not_claimed',s['sources'][26]['access']=='METADATA_ONLY' and not read('sessions/S013/SOURCE_MANIFEST.json')['original_OlsonII_body_read'])
 check('original_Ga4_actual_source',s['sources'][27]['access']=='PROOF_INSPECTED')
 changed=subprocess.check_output(['git','diff','--name-only',base],cwd=ROOT,text=True).splitlines()
 check('historical_sessions_not_modified',not any(re.match(r'(sessions/S00[1-9]/|sessions/S01[0-2]/|validation/S01[0-2]_)',x) for x in changed))
 result={'session':'S013','kind':'ADMINISTRATIVE_ONLY','result':'PASS','checks':checks,'checks_passed':len(checks),'mathematical_certification':False,'hosted_ci_pass':False,'author_code_executed':False,'limits':['Complete scoped hand proof is manually reviewed, not program-certified.','Rank-two prerequisites and B=>C implication independently proved; unconditional Reiher Property B and stronger coefficient remain unproved.','Zero hosted checks do not constitute CI PASS.','Raw owner chat transport bytes unavailable; no transport hash claimed.'],'errors':[]}
 (ROOT/'validation/S013_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
 print('S013 administrative PASS:',len(checks),'checks; NOT hosted CI or mathematical certification')
if __name__=='__main__':main()
