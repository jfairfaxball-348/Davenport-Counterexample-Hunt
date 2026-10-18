"""S111 validator (administrative): claims delta, unchanged records, two-algorithm agreement
for the TWO(a) checks, exact-test pass, state consistency.
python -I validation/validate_s111.py <entry_sha>"""
import hashlib, json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "f8c9df20c687e0cc8ecabfe395d52526a365283d"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
def sha(p): return hashlib.sha256(lf(open(p, "rb").read())).hexdigest()
r = {}

cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
assert len(cl["claims"]) == 373 and cl["claims"][:367] == old["claims"]
assert [c["id"] for c in cl["claims"][367:]] == [f"CLM-{i:04d}" for i in range(368, 374)]
assert [c["status"] for c in cl["claims"][367:]] == ["PROGRAMME_PROVED"] * 5 + ["COMPUTED_EXACT"]
r["claims"] = "373; first 367 identical to entry; CLM-0368..0372 PROGRAMME_PROVED, CLM-0373 COMPUTED_EXACT"

for p in ("catalogue/sources.json", "frontier/frontier.json", "frontier/FRONTIER.md", "catalogue/SOURCES.md",
          "tools/zsf/checker_a.py", "tools/zsf/checker_b.py", "tools/zsf/support5_a.py", "tools/zsf/support5_b.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged"] = "sources, frontier, checkers, support-5 tools"

two = {}
for a, inst, fails in ((3, 65780, 5616), (4, 271560, 432), (5, 337260, 7188)):
    A = load(f"sessions/S111/two_a{a}_A.json"); B = load(f"sessions/S111/two_a{a}_B.json")
    assert A["algorithm"] == "A" and B["algorithm"] == "B"
    assert A["families"] == B["families"] and A["instances_total"] == B["instances_total"] == inst
    assert A["failure_count"] == B["failure_count"] == fails and not A["TWO_holds_on_all_instances"]
    assert A["decision_stream_sha256"] == B["decision_stream_sha256"]
    two[a] = {"instances": inst, "failures": fails, "stream": A["decision_stream_sha256"][:16]}
r["TWO_a"] = two

t = load("sessions/S111/S111_TESTS.json")
assert t["overall"] == "PASS" and all(t[k]["pass"] for k in t if k.startswith("T"))
c4 = t["T4_odd_packing_obstructions"]["cases"]
assert c4["a3_b5"]["max_packing"] == 12 and c4["a3_b5"]["needed_D(C_b^3)"] == 13
assert c4["a5_b3"]["max_packing"] == 6 and c4["a5_b3"]["needed_D(C_b^3)"] == 7
r["tests"] = "T1..T5 PASS; packing 12<13 (a=3), 6<7 (a=5)"

r["tool_sha256_lf"] = {p: sha(p) for p in ("tools/zsf/two_disjoint.py", "tools/zsf/test_s111.py")}

s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S111" and s["recommended_next_session"] == "S112"
assert s["counterexample_status"] == "NONE_CLAIMED"
c = s["counterexample_hunt_strategy"]
assert c["number_of_fallback_sessions"] == 6 and c["fallback_sessions"][-1] == "S111"
assert c["priority"] == "SATURATION_FALLBACK" and c["campaigns_active"] == [] and c["campaigns_preregistered"] == []
assert (c["number_of_setup_sessions"], c["number_of_active_search_sessions"],
        c["number_of_completed_materially_distinct_bounded_rounds"]) == (1, 2, 2)
assert s["s111_result"]["claims_total"] == 373
assert os.listdir("candidates") == ["README.md"]
r["state"] = "consistent; search counters frozen (1, 2, 2); fallback sessions 6"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
