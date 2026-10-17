"""S106 repository consistency validator (administrative, not mathematical
certification).  Run from repo root: python -I validation/validate_s106.py <entry_sha>"""
import json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "7965795c7b948fbd670c7925bafb440e9b4cf124"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
r = {}
cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
ids = [c["id"] for c in cl["claims"]]
assert len(ids) == len(set(ids)) == 352 and cl["claims"][:347] == old["claims"]
assert ids[-5:] == [f"CLM-03{k}" for k in range(48, 53)]
st = {c["id"]: c["status"] for c in cl["claims"]}
assert [st[f"CLM-03{k}"] for k in range(48, 53)] == ["PROGRAMME_PROVED"] * 4 + ["SOURCE_STATED"]
assert all(c["status"] in cl["status_enum"] for c in cl["claims"])
r["claims"] = "352; first 347 identical to entry; CLM-0348..0351 PROGRAMME_PROVED, CLM-0352 SOURCE_STATED"
src = load("catalogue/sources.json"); olds = json.loads(git_show("catalogue/sources.json"))
assert src["sources"][:32] == olds["sources"] and [s["id"] for s in src["sources"][32:]] == ["SRC-0033", "SRC-0034"]
assert all(s["access"] in src["access_enum"] for s in src["sources"])
r["sources"] = "34; first 32 identical to entry"
for p in ("frontier/frontier.json", "tools/zsf/checker_a.py", "tools/zsf/checker_b.py", "tools/zsf/lns_engine.py", "tools/zsf/ils_engine.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged"] = "frontier.json, checkers, engines"
t = load("sessions/S106/QUOTIENT_LEMMA_TESTS.json")
assert t["overall"] == "PASS" and t["clm0348_basis_completions_checked"] == 40567
assert all(v == 2 * n - 2 for n in (3, 4) for v in t[f"clm0350_exhaustive_n{n}_max_T"].values())
r["lemma_tests"] = "PASS"
s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S106" and s["recommended_next_session"] == "S107"
h = s["counterexample_hunt_strategy"]
assert h["priority"] == "SATURATION_FALLBACK" and h["number_of_fallback_sessions"] == 1
assert h["number_of_active_search_sessions"] == 2 and h["number_of_completed_materially_distinct_bounded_rounds"] == 2
assert h["campaigns_active"] == [] and s["counterexample_status"] == "NONE_CLAIMED"
r["state"] = "consistent"
assert os.listdir("candidates") == ["README.md"]
assert not os.path.exists("campaigns/CAM-0006")
r["no_new_campaign_or_candidate"] = True
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
