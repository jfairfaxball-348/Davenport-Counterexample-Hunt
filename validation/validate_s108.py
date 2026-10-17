"""S108 repository consistency validator (administrative, not mathematical
certification).  Run from repo root: python -I validation/validate_s108.py <entry_sha>"""
import json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "9073184067b0820ebef1e72a0e589b33883e429b"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
r = {}
cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
ids = [c["id"] for c in cl["claims"]]
assert len(ids) == len(set(ids)) == 360 and cl["claims"][:357] == old["claims"]
assert [c["status"] for c in cl["claims"][357:]] == ["PROGRAMME_PROVED"] * 3
assert all(c["status"] in cl["status_enum"] for c in cl["claims"])
r["claims"] = "360; first 357 identical to entry"
src = load("catalogue/sources.json"); olds = json.loads(git_show("catalogue/sources.json"))
assert src["sources"] == olds["sources"] and "s108_audit" in src
r["sources"] = "34 records identical to entry; s108_audit added"
for p in ("frontier/frontier.json", "tools/zsf/checker_a.py", "tools/zsf/checker_b.py", "tools/zsf/lns_engine.py",
          "tools/zsf/ils_engine.py", "tools/zsf/test_quotient_lemmas.py", "tools/zsf/test_transfer_lemmas.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged"] = "frontier.json, checkers, engines, S106/S107 tests"
t = load("sessions/S108/SMALL_SUPPORT_TESTS.json")
assert t["overall"] == "PASS" and t["clm0358_criterion_agreements"] == 5200
assert t["exhaustive_4_supports_C2^3_max_len"] == 3 and t["exhaustive_4_supports_C3^3_max_len"] == 6
r["lemma_tests"] = "PASS"
s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S108" and s["recommended_next_session"] == "S109"
h = s["counterexample_hunt_strategy"]
assert h["priority"] == "SATURATION_FALLBACK" and h["number_of_fallback_sessions"] == 3 and h["search_reopen_condition_met"] is False
assert h["number_of_active_search_sessions"] == 2 and h["campaigns_active"] == [] and s["counterexample_status"] == "NONE_CLAIMED"
r["state"] = "consistent"
assert os.listdir("candidates") == ["README.md"] and not os.path.exists("campaigns/CAM-0006")
r["no_new_campaign_or_candidate"] = True
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
