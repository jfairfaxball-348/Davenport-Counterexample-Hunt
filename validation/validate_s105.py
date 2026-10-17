"""S105 repository consistency validator (administrative, not mathematical
certification).  Run from repo root: python -I validation/validate_s105.py <entry_sha>"""
import hashlib, json, os, subprocess, sys
sys.path.insert(0, "tools/zsf")
import checker_a as A, checker_b as B

entry = sys.argv[1] if len(sys.argv) > 1 else "35ee471d8f48d6e183c10916ab8b2fd006148497"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
def sha(p): return hashlib.sha256(lf(open(p, "rb").read())).hexdigest()
def H(d): return hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest()
r = {}
for p in ("catalogue/claims.json", "catalogue/sources.json", "frontier/frontier.json",
          "campaigns/CAM-0004/PREREGISTRATION.json", "campaigns/CAM-0005/PREREGISTRATION.json",
          "campaigns/CAM-0002/RESULT.json", "campaigns/CAM-0003/RESULT.json", "tools/zsf/lns_engine.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
r["unchanged_vs_entry"] = "claims(347), sources(32), frontier.json, CAM-0004/0005 preregistrations, round-1 results, R2 engine"
assert len(load("catalogue/claims.json")["claims"]) == 347
for cam, n, tgt in (("CAM-0004", 15, 43), ("CAM-0005", 20, 58)):
    pre = load(f"campaigns/{cam}/PREREGISTRATION.json"); res = load(f"campaigns/{cam}/RESULT.json")
    for p, h in pre["code_sha256"].items():
        assert sha(p) == h, (cam, p)
    mods = (n, n, n)
    assert sorted(res["workers"]) == [str(s) for s in pre["budget"]["seeds"]]
    for s, w in res["workers"].items():
        b = lf(open(f"campaigns/{cam}/checkpoints/seed-{s}.jsonl", "rb").read())
        assert hashlib.sha256(b).hexdigest() == res["full_log_sha256"][f"seed-{s}.jsonl"]["sha256_lf_normalised_git_blob"]
        recs = [json.loads(l) for l in b.decode().splitlines() if l.strip()]
        st, end = recs[0], recs[-1]
        reg = dict(n=n, target=tgt, seed=int(s), init=pre["budget"]["init_per_seed"][s], iterations=1200, walltime=7200,
                   m2=12, cap_a=64, tabu_len=8, stall=200, engine="R2-LNS-1.0")
        assert H(reg) == pre["parameter_sha256_per_worker"][s]          # registered (int walltime)
        assert st["params"] == reg                                      # values equal
        assert end["param_hash"] == H(dict(reg, walltime=7200.0))       # engine (float walltime)
        assert end["kind"] == "end" and end["status"] == w["status"] == "BUDGET_EXHAUSTED" and end["iterations_done"] == 1200
        best = [tuple(g) for g in end["best"]]
        assert len(best) == 3 * n - 3 == w["best_len"]
        assert A.is_zero_sumfree(best, mods)[0] and B.is_zero_sumfree(best, mods)
        assert not any(x["kind"] == "CANDIDATE_QUARANTINE" for x in recs)
    r[cam] = f"6 workers BUDGET_EXHAUSTED, best {3*n-3}, params equal registered values, logs hash-matched, A/B rechecked"
st = load("authoritative/STATE.json")
assert st["last_completed_session"] == "S105" and st["recommended_next_session"] == "S106"
h = st["counterexample_hunt_strategy"]
assert h["priority"] == "SATURATION_FALLBACK" and h["number_of_active_search_sessions"] == 2
assert h["number_of_completed_materially_distinct_bounded_rounds"] == 2 and h["campaigns_active"] == [] and h["campaigns_preregistered"] == []
assert st["campaign_active"] is None and st["counterexample_status"] == "NONE_CLAIMED"
r["state"] = "consistent; priority SATURATION_FALLBACK"
assert load("sessions/S105/TEST_OUTPUT.json")["overall"] == "PASS"
assert load("sessions/S105/LNS_PREFLIGHT.json") == load("sessions/S104/LNS_PREFLIGHT.json")
r["tests"] = "PASS; preflight identical to S104"
assert os.listdir("candidates") == ["README.md"]
r["candidates_dir"] = "README only"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
