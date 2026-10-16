"""S103 repository consistency validator (administrative, not mathematical
certification).  Run from repo root: python -I validation/validate_s103.py <entry_sha>"""
import hashlib, json, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "13ce00e0f04715418f99687a858892f02f3457b4"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def sha(p): return hashlib.sha256(open(p, "rb").read().replace(b"\r\n", b"\n")).hexdigest()
r = {}
claims = load("catalogue/claims.json")["claims"]
ids = [c["id"] for c in claims]
assert len(ids) == len(set(ids)) == 346 and ids[-2:] == ["CLM-0345", "CLM-0346"]
assert all(c["status"] in load("catalogue/claims.json")["status_enum"] for c in claims)
r["claims"] = 346
src = load("catalogue/sources.json"); old = json.loads(git_show("catalogue/sources.json"))
assert src["sources"][:29] == old["sources"] and len(src["sources"]) == 32
assert all(s["access"] in src["access_enum"] for s in src["sources"])
r["sources"] = "32; original 29 identical to entry"
fr_now = open("frontier/frontier.json", "rb").read().replace(b"\r\n", b"\n")
assert fr_now == git_show("frontier/frontier.json").replace(b"\r\n", b"\n")
r["frontier_json_unchanged"] = True
for cam in ("CAM-0002", "CAM-0003"):
    d = load(f"campaigns/{cam}/PREREGISTRATION.json")
    for p, h in d["code_sha256"].items():
        assert sha(p) == h, (cam, p)
    assert d["status"] == "PREREGISTERED_NOT_ACTIVATED" and d["completeness_class"] == "HEURISTIC"
r["prereg_code_hashes_match"] = True
st = load("authoritative/STATE.json")
assert st["last_completed_session"] == "S103" and st["recommended_next_session"] == "S104"
h = st["counterexample_hunt_strategy"]
assert h["priority"] == "SEARCH_FIRST" and h["number_of_active_search_sessions"] == 0 and h["number_of_completed_materially_distinct_bounded_rounds"] == 0
assert st["campaign_active"] is None and st["counterexample_status"] == "NONE_CLAIMED"
r["state"] = "consistent"
t = load("sessions/S103/TEST_OUTPUT.json"); assert t["overall"] == "PASS"
p = load("sessions/S103/ENGINE_PREFLIGHT.json"); assert p["overall"] == "PASS"
r["tests"] = "PASS"
import os
assert os.listdir("candidates") == ["README.md"]
r["candidates_dir"] = "README only"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
