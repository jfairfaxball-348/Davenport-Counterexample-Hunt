"""S112 validator (administrative): claims delta, unchanged records, sieve agreement,
hand-proof arithmetic re-check, tests, state.
python -I validation/validate_s112.py <entry_sha>"""
import hashlib, itertools, json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "890217c338f7936f035e3d299d7226d153db0307"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
def sha(p): return hashlib.sha256(lf(open(p, "rb").read())).hexdigest()
r = {}
cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
assert len(cl["claims"]) == 378 and cl["claims"][:373] == old["claims"]
assert [c["status"] for c in cl["claims"][373:]] == ["PROGRAMME_PROVED", "COMPUTED_EXACT", "PROGRAMME_PROVED",
                                                     "PROGRAMME_PROVED", "COMPUTED_EXACT"]
r["claims"] = "378; first 373 identical to entry"
for p in ("catalogue/sources.json", "frontier/frontier.json", "frontier/FRONTIER.md", "catalogue/SOURCES.md",
          "tools/zsf/checker_a.py", "tools/zsf/checker_b.py", "tools/zsf/two_disjoint.py", "tools/zsf/test_s111.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged"] = "sources, frontier, checkers, S111 tools"
sv = load("sessions/S112/ROUTE_SIEVE.json")["cases"]
expect = {"12": 6, "15": 5, "18": 6, "20": 6, "21": 5, "28": 5, "30": 4, "33": 4, "35": 4}
for n, k in expect.items():
    assert sv[n]["A_equals_B"] and sv[n]["all_supports_excluded_up_to"] == k, n
assert sv["15"]["surviving_patterns_by_k"]["6"] == 5 and sv["20"]["surviving_patterns_by_k"]["7"] == 139
r["sieve"] = "A = B for all n; exclusions as claimed"
# independent re-check of the CLM-0376 hand-proof arithmetic: both routes failing is impossible
bad = [al for al in itertools.combinations_with_replacement(range(15), 5) if sum(al) == 43
       and sum(2 - a % 3 for a in al) == 0 and sum(4 - a % 5 for a in al) == 2]
assert bad == []
r["CLM-0376_arithmetic"] = "no alpha with both route-3 and route-5 failure conditions"
t = load("sessions/S112/S112_TESTS.json")
assert t["overall"] == "PASS"
c2 = t["T2_route_soundness_constructive"]["cases"]
assert all(v["closing_route_runs"] == v["verified"] > 0 for v in c2.values())
r["tests"] = "T1 D2(C2^3)=7; T2 %d closing-route runs all verified" % sum(v["verified"] for v in c2.values())
r["tool_sha256_lf"] = {p: sha(p) for p in ("tools/zsf/route_sieve.py", "tools/zsf/test_s112.py")}
s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S112" and s["recommended_next_session"] == "S113"
assert s["counterexample_status"] == "NONE_CLAIMED"
c = s["counterexample_hunt_strategy"]
assert c["number_of_fallback_sessions"] == 7 and c["fallback_sessions"][-1] == "S112"
assert c["campaigns_active"] == [] and c["campaigns_preregistered"] == []
assert (c["number_of_setup_sessions"], c["number_of_active_search_sessions"],
        c["number_of_completed_materially_distinct_bounded_rounds"]) == (1, 2, 2)
assert os.listdir("candidates") == ["README.md"]
r["state"] = "consistent; counters frozen; fallback sessions 7"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
