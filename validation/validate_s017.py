#!/usr/bin/env python3
"""S017 administrative integrity only; no mathematical computation or author code."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
checks={}
def check(name, condition):
    checks[name]=bool(condition)
    if not condition: raise AssertionError(name)
def read(p): return json.loads((ROOT/p).read_text())
def original(base,p): return subprocess.check_output(['git','show',base+':'+p],cwd=ROOT)
def main():
    for p in ROOT.rglob('*.json'):
        if '.git' not in p.parts: json.loads(p.read_text())
    check('all_json_parses',True)
    c=read('catalogue/claims.json'); s=read('catalogue/sources.json'); f=read('frontier/frontier.json')
    st=read('authoritative/STATE.json'); e=read('sessions/S017/ENTRY_REVIEW.json'); v=read('validation/S017_REVIEW.json')
    base=e['entry_main']; oldc=json.loads(original(base,'catalogue/claims.json')); olds=json.loads(original(base,'catalogue/sources.json')); oldf=json.loads(original(base,'frontier/frontier.json'))
    si=[x['id'] for x in s['sources']]; ci=[x['id'] for x in c['claims']]
    check('28_unique_source_ids',si==[f'SRC-{i:04d}' for i in range(1,29)])
    check('103_unique_claim_ids',ci==[f'CLM-{i:04d}' for i in range(1,104)])
    check('all_102_old_claim_objects_preserved',c['claims'][:102]==oldc['claims'])
    check('all_source_access_classes_preserved',[(x['id'],x['access']) for x in s['sources']]==[(x['id'],x['access']) for x in olds['sources']])
    check('source_identity_fields_preserved',all(all(x[k]==y[k] for k in y if k not in ['notes','accessed']) for x,y in zip(s['sources'],olds['sources'])))
    check('notes_append_only',all(x['notes'].startswith(y['notes']) for x,y in zip(s['sources'],olds['sources'])))
    check('enum_validity',all(x['status'] in c['status_enum'] for x in c['claims']) and all(x['access'] in s['access_enum'] for x in s['sources']))
    check('claim_source_refs',all(set(x.get('source_ids',[]))<=set(si) for x in c['claims']))
    check('new_claim_narrow_original_scope',c['claims'][-1]['id']=='CLM-0103' and c['claims'][-1]['origin']=='research/S017_REIHER_PROPOSITION_8_1.md' and c['claims'][-1]['status']=='PROGRAMME_PROVED')
    check('inherited_claims_quarantined',all(x['status']=='INHERITED_UNVERIFIED' for x in c['claims'][:37]))
    check('historical_CLM0082_source_stated',c['claims'][81]['status']=='SOURCE_STATED')
    check('no_computed_or_formal_claims',not any(x['status'] in ['COMPUTED_EXACT','FORMALLY_CERTIFIED'] for x in c['claims']))
    for filename,items,key in [('catalogue/CLAIMS.md',c['claims'],'status'),('catalogue/SOURCES.md',s['sources'],'access')]:
        text=(ROOT/filename).read_text()
        check(filename+'_old_bytes_prefix_preserved',text.encode().startswith(original(base,filename).rstrip()))
        check(filename+'_one_section_per_id',all(len(re.findall(r'^## '+x['id']+r' — ',text,re.M))==1 for x in items))
        for x in items:
            section=text.split('## '+x['id']+' — ',1)[1].split('\n## ',1)[0]
            check(x['id']+'_markdown_class',x[key] in section)
    check('all30_frontier_row_objects_preserved',f['rows']==oldf['rows'])
    check('unique30_rows', [x['n'] for x in f['rows']]==list(range(1,31)))
    md=(ROOT/'frontier/FRONTIER.md').read_text()
    table={int(cols[1]):cols[2:] for line in md.splitlines() if re.match(r'^\| \d+ \|',line) for cols in [[x.strip() for x in line.split('|')]]}
    check('markdown30_rows',len(table)==30)
    for row in f['rows']:
        check('row'+str(row['n'])+'_numeric_status_evidence_mirror',table[row['n']][:5]==[row['group'],str(row['d_star']),row['reported_bound'],row['provisional_status'],', '.join(row['evidence'])])
        check('row'+str(row['n'])+'_endpoint_encoding',row['reported_bound']==(str(row['lower_bound']) if row['lower_bound']==row['upper_bound'] else str(row['lower_bound'])+'..'+str(row['upper_bound'])))
    check('frontier_refs',all(set(x['evidence'])<=set(si+ci)|{'TRIVIAL_GROUP'} for x in f['rows']))
    known=set(si+ci)
    for p in list((ROOT/'research').glob('*.md'))+list((ROOT/'sessions/S017').glob('*.md')):
        check(str(p.relative_to(ROOT))+'_source_refs',set(re.findall(r'\bSRC-\d{4}\b',p.read_text()))<=set(si))
        check(str(p.relative_to(ROOT))+'_claim_refs',set(re.findall(r'\bCLM-\d{4}\b',p.read_text()))<=known)
    check('five_intervals',[(x['n'],x['lower_bound'],x['upper_bound']) for x in f['rows'] if x['lower_bound']!=x['upper_bound']]==[(15,43,45),(20,58,59),(21,61,63),(28,82,83),(30,88,90)])
    check('gate_held',st['last_completed_session']=='S017' and st['recommended_next_session']=='S018' and st['phases']['1']['status']=='IN_PROGRESS' and all(st['phases'][str(i)]['status']=='NOT_STARTED' for i in [2,3]))
    check('campaign_blocked',st['campaign_active'] is None and all(x in (ROOT/'campaigns/REGISTRY.md').read_text() for x in ['S017','PROPOSED / NOT RUNNING','BLOCKED','16']))
    check('all_spine_synced',all('S017' in (ROOT/p).read_text() for p in ['authoritative/START_HERE.md','authoritative/DECISION_LOG.md','docs/PHASE_GATE_LEDGER.md','docs/SESSION_LEDGER.md','docs/FAILURE_AND_LESSON_LEDGER.md','research/FOUNDATIONS.md','catalogue/SOURCES.md','catalogue/CLAIMS.md','frontier/FRONTIER.md','campaigns/REGISTRY.md']))
    inp=(ROOT/'sessions/S017/INPUT.md').read_bytes(); im=read('sessions/S017/INPUT_MANIFEST.json')
    check('input_committed_handoff_byte_exact',inp==original(base,'authoritative/NEXT_SESSION_PROMPT.md') and len(inp)==im['committed_handoff_bytes'] and hashlib.sha256(inp).hexdigest()==im['committed_handoff_sha256'])
    priorclose=original(base,'sessions/S016/CLOSEOUT.md'); embedded=priorclose.split(b'<!-- S017_PROMPT_START -->\n',1)[1].split(b'<!-- S017_PROMPT_END -->',1)[0]
    check('previous_closeout_incoming_byte_exact',embedded==inp)
    check('separate_invocation_and_no_raw_hash',(ROOT/'sessions/S017/OWNER_INVOCATION.md').read_bytes()==inp and not im['raw_chat_transport_hash_claimed'])
    fut=(ROOT/'authoritative/NEXT_SESSION_PROMPT.md').read_bytes(); close=(ROOT/'sessions/S017/CLOSEOUT.md').read_bytes(); fm=read('sessions/S017/FUTURE_HANDOFF_MANIFEST.json')
    check('outgoing_handoff_byte_exact',close.split(b'<!-- S018_PROMPT_START -->\n',1)[1].split(b'<!-- S018_PROMPT_END -->',1)[0]==fut and hashlib.sha256(fut).hexdigest()==fm['sha256'] and len(fut)==fm['bytes'])
    check('S018_strictly_unexecuted',b'FUTURE, UNEXECUTED' in fut and not v['future_session_executed'] and not (ROOT/'sessions/S018').exists())
    head=e['prior_s016_head']; raw=subprocess.check_output(['git','show','-s','--format=%P%n%T',head],cwd=ROOT,text=True).splitlines()
    merge=subprocess.check_output(['git','show','-s','--format=%P%n%T',base],cwd=ROOT,text=True).splitlines()
    check('prior_single_parent_and_two_parent_merge',raw[0]==e['prior_s016_head_parent'] and merge[0].split()==e['prior_merge_parents'])
    check('prior_exact_tree_identity',raw[1]==merge[1]==e['entry_tree'])
    check('prior_atomic_count',int(subprocess.check_output(['git','rev-list','--count',e['prior_s016_head_parent']+'..'+head],cwd=ROOT))==e['prior_pr_commit_count']==1)
    check('empty_hosted_checks_not_pass',not e['ci_pass_claimed'] and not v['hosted_ci_pass'] and e['hosted_action_runs']==e['hosted_action_jobs']==e['check_runs']==e['status_contexts']==0)
    check('access_errors_not_zero',e['branch_protection_api'].startswith('HTTP403') and 'not evidence of zero' in e['workflow_listing_api'])
    check('no_source_execution_or_math_search',not v['source_program_execution'] and v['mathematical_numerical_searches']==0 and not read('sessions/S017/SOURCE_MANIFEST.json')['author_code_executed'])
    check('scope_precise',v['proposition8_1_independently_proved'] and not any(v[k] for k in ['section9_proof_executed','unconditional_property_B_proved','unconditional_property_C_proved','rank_three_eta7_unconditional','stronger_coefficient_proved']))
    changed=subprocess.check_output(['git','diff','--name-only',base],cwd=ROOT,text=True).splitlines()
    check('old_session_records_untouched',not any(re.match(r'(sessions/S0(?:0[1-9]|1[0-6])/|validation/S0(?:0[1-9]|1[0-6])_)',x) for x in changed))
    check('no_primary_PDF_TeX_in_repository',not any(p.suffix in ['.pdf','.tex'] for p in ROOT.rglob('*') if '.git' not in p.parts))
    check('no_local_workflow_files',not list((ROOT/'.github/workflows').glob('*')))
    result={'session':'S017','kind':'ADMINISTRATIVE_ONLY','result':'PASS','checks':checks,'checks_passed':len(checks),'mathematical_certification':False,'hosted_ci_pass':False,'errors':[],'limits':['Manual symbolic proof separately reviewed; not verified by this administrative program.','Zero hosted checks NOT CI PASS.','No raw chat transport hash.']}
    (ROOT/'validation/S017_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print('S017 administrative PASS:',len(checks),'checks; NOT hosted CI or mathematical certification')
if __name__=='__main__':main()
