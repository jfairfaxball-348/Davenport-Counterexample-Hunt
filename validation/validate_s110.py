"""S110 validator (administrative): coverage, log hashes, two-algorithm agreement.
python -I validation/validate_s110.py <entry_sha>"""
import hashlib, json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "e3ecb17b015a2a0dba84f777f2f26083b2591390"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
r = {}
cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
assert len(cl["claims"]) == 367 and cl["claims"][:365] == old["claims"]
assert [c["status"] for c in cl["claims"][365:]] == ["COMPUTED_EXACT"] * 2
r["claims"] = "367; first 365 identical to entry"
for p in ("catalogue/sources.json", "frontier/frontier.json", "tools/zsf/support5_a.py", "tools/zsf/support5_b.py",
          "campaigns/CAM-0006/PREREGISTRATION.json", "campaigns/CAM-0007/PREREGISTRATION.json"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged"] = "sources, frontier, tools, preregistrations"
for cam, n in (("CAM-0006", 15), ("CAM-0007", 20)):
    pre = load(f"campaigns/{cam}/PREREGISTRATION.json"); res = load(f"campaigns/{cam}/RESULT.json")
    assert res["campaign_status"] == "COMPLETED_EXHAUSTIVE_NO_HIT" and res["two_algorithm_agreement"]
    for alg in ("A", "B"):
        x = res["algorithms"][alg]
        tot = 0
        for s in x["shards"]:
            k = s["shard"]
            out = load(f"campaigns/{cam}/checkpoints/{alg.lower()}-s{k}.json")
            raw = lf(open(f"campaigns/{cam}/checkpoints/{alg.lower()}-s{k}.jsonl", "rb").read())
            assert hashlib.sha256(raw).hexdigest() == x["log_sha256"][f"{alg.lower()}-s{k}.jsonl"]["sha256_lf"]
            recs = [json.loads(l) for l in raw.decode().splitlines() if l.strip()]
            assert recs[-1]["kind"] == "end" and not any(q["kind"] == "AT_OR_ABOVE" for q in recs)
            assert s["status"] == "COMPLETE" and s["exit"] == 0 and out["max_length"] <= 3 * n - 3
            tot += out["pairs_evaluated"]
        assert tot == pre["algorithms"][alg]["expected_pairs_total"] == x["pairs_evaluated_total"]
        assert x["max_optimum"] == 3 * n - 3
    r[cam] = "complete, full coverage both algorithms, max 3n-3, no hit, logs hash-matched"
s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S110" and s["recommended_next_session"] == "S111" and s["counterexample_status"] == "NONE_CLAIMED"
assert os.listdir("candidates") == ["README.md"]
r["state"] = "consistent"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
