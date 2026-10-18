"""S113 validator (administrative): claims delta, unchanged records, hand-proof arithmetic
re-check, lemma tests, state.
python -I validation/validate_s113.py <entry_sha>"""
import hashlib, itertools, json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "da61638f22f51cf9fcd7c589c5ca8aa4312353a5"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
def sha(p): return hashlib.sha256(lf(open(p, "rb").read())).hexdigest()
r = {}
cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
assert len(cl["claims"]) == 383 and cl["claims"][:378] == old["claims"]
assert [c["id"] for c in cl["claims"][378:]] == ["CLM-0%d" % i for i in range(379, 384)]
assert all(c["status"] == "PROGRAMME_PROVED" for c in cl["claims"][378:])
r["claims"] = "383; first 378 identical to entry"
for p in ("catalogue/sources.json", "frontier/frontier.json", "frontier/FRONTIER.md", "catalogue/SOURCES.md",
          "tools/zsf/checker_a.py", "tools/zsf/checker_b.py", "tools/zsf/route_sieve.py", "tools/zsf/test_s112.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged"] = "sources, frontier, checkers, S112 tools"
# independent re-check of the two small hand-proof cases
def W(A, B, wmin):
    n = A * B
    return [w for w in itertools.combinations_with_replacement(range(wmin, n), 5) if sum(w) == 2 * n - 3
            and sum(x % A for x in w) == A - 3 and sum(x % B for x in w) == B - 3]
assert W(3, 5, 0) == [] and W(3, 7, 1) == []
assert [a for a in itertools.combinations_with_replacement(range(1, 19, 2), 6) if sum(a) == 58
        and sum(1 for x in a if x % 4 == 3) in (4, 6) and sum((-(x + 1)) % 5 for x in a) in (1, 6)] == []
r["hand_proof_arithmetic"] = "(3,5) w>=0, (3,7) w>=1 and the n=20 (B1)-(B4) system have no solution"
t = load("sessions/S113/S113_LEMMA_TESTS.json")
assert t["overall"] == "PASS" and all(t[k]["pass"] for k in t if k.startswith("L"))
r["lemma_tests"] = "L1-L5 PASS (evidence only)"
r["tool_sha256_lf"] = {p: sha(p) for p in ("tools/zsf/test_s113.py",)}
s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S113" and s["recommended_next_session"] == "S114"
assert s["counterexample_status"] == "NONE_CLAIMED" and s["s113_result"]["claims_total"] == 383
c = s["counterexample_hunt_strategy"]
assert c["number_of_fallback_sessions"] == 8 and c["fallback_sessions"][-1] == "S113"
assert c["campaigns_active"] == [] and c["campaigns_preregistered"] == []
assert (c["number_of_setup_sessions"], c["number_of_active_search_sessions"],
        c["number_of_completed_materially_distinct_bounded_rounds"]) == (1, 2, 2)
assert os.listdir("candidates") == ["README.md"]
for p in ("INPUT.md", "INPUT_MANIFEST.json", "PLAN.md", "SOURCE_MANIFEST.json", "REVIEW.md", "CLOSEOUT.md"):
    assert os.path.exists("sessions/S113/" + p), p
r["state"] = "consistent; counters frozen; fallback sessions 8"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
