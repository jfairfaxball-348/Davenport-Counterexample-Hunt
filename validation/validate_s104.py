"""S104 repository consistency validator (administrative, not mathematical
certification).  Run from repo root: python -I validation/validate_s104.py <entry_sha>"""
import hashlib, json, os, subprocess, sys
sys.path.insert(0, "tools/zsf")
import checker_a as A, checker_b as B

entry = sys.argv[1] if len(sys.argv) > 1 else "eec2f529c3c5fe5cb71a27eb83d52c7696c8569a"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def sha(p): return hashlib.sha256(open(p, "rb").read().replace(b"\r\n", b"\n")).hexdigest()
r = {}
claims = load("catalogue/claims.json")["claims"]
ids = [c["id"] for c in claims]
assert len(ids) == len(set(ids)) == 347 and ids[-1] == "CLM-0347"
old = json.loads(git_show("catalogue/claims.json"))["claims"]
assert claims[:346] == old
r["claims"] = "347; first 346 identical to entry"
src = load("catalogue/sources.json")
assert src == json.loads(git_show("catalogue/sources.json"))
r["sources"] = "32 unchanged"
assert open("frontier/frontier.json", "rb").read().replace(b"\r\n", b"\n") == git_show("frontier/frontier.json").replace(b"\r\n", b"\n")
r["frontier_json_unchanged"] = True
for cam in ("CAM-0002", "CAM-0003"):
    assert open(f"campaigns/{cam}/PREREGISTRATION.json", "rb").read().replace(b"\r\n", b"\n") == git_show(f"campaigns/{cam}/PREREGISTRATION.json").replace(b"\r\n", b"\n")
    pre = load(f"campaigns/{cam}/PREREGISTRATION.json"); res = load(f"campaigns/{cam}/RESULT.json")
    for p, h in pre["code_sha256"].items():
        assert sha(p) == h, (cam, p)
    n = res["n"]; mods = (n, n, n)
    assert sorted(res["workers"]) == [str(s) for s in pre["budget"]["seeds"]]
    for s, w in res["workers"].items():
        lines = open(f"campaigns/{cam}/checkpoints/seed-{s}.jsonl", "rb").read().replace(b"\r\n", b"\n")
        assert hashlib.sha256(lines).hexdigest() == res["full_log_sha256"][f"seed-{s}.jsonl"]["sha256_lf_normalised_git_blob"]
        recs = [json.loads(l) for l in lines.decode().splitlines() if l.strip()]
        end = recs[-1]
        assert end["kind"] == "end" and end["param_hash"] == pre["parameter_sha256_per_worker"][s]
        assert end["status"] == w["status"] == "BUDGET_EXHAUSTED" and end["iterations_done"] == 200000
        best = [tuple(g) for g in end["best"]]
        assert len(best) == 3 * n - 3 == w["best_len"]
        assert A.is_zero_sumfree(best, mods)[0] and B.is_zero_sumfree(best, mods)
        assert not any(x["kind"] == "CANDIDATE_QUARANTINE" for x in recs)
    r[cam] = f"6 workers BUDGET_EXHAUSTED, best {3*n-3}, logs hash-matched, A/B rechecked"
for cam in ("CAM-0004", "CAM-0005"):
    d = load(f"campaigns/{cam}/PREREGISTRATION.json")
    for p, h in d["code_sha256"].items():
        assert sha(p) == h, (cam, p)
    assert d["status"] == "PREREGISTERED_NOT_ACTIVATED" and d["completeness_class"] == "HEURISTIC" and d["round"] == 2
    assert not os.path.exists(f"campaigns/{cam}/checkpoints")
r["round2_prereg_code_hashes_match_and_not_run"] = True
st = load("authoritative/STATE.json")
assert st["last_completed_session"] == "S104" and st["recommended_next_session"] == "S105"
h = st["counterexample_hunt_strategy"]
assert h["priority"] == "SEARCH_FIRST" and h["number_of_active_search_sessions"] == 1
assert h["number_of_completed_materially_distinct_bounded_rounds"] == 1 and h["number_of_setup_sessions"] == 1
assert st["campaign_active"] is None and st["counterexample_status"] == "NONE_CLAIMED"
r["state"] = "consistent"
assert load("sessions/S104/TEST_OUTPUT.json")["overall"] == "PASS"
assert load("sessions/S104/LNS_PREFLIGHT.json")["overall"] == "PASS"
r["tests"] = "PASS"
assert os.listdir("candidates") == ["README.md"]
r["candidates_dir"] = "README only"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
