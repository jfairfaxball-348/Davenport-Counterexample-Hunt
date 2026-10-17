"""S109 repository consistency validator (administrative).  python -I validation/validate_s109.py <entry_sha>"""
import hashlib, json, os, subprocess, sys

entry = sys.argv[1] if len(sys.argv) > 1 else "b70c5b113579a653011e78393cc8942f98e73240"
def load(p): return json.load(open(p, encoding="utf-8"))
def git_show(path): return subprocess.run(["git", "show", f"{entry}:{path}"], capture_output=True, check=True).stdout
def lf(b): return b.replace(b"\r\n", b"\n")
def sha(p): return hashlib.sha256(lf(open(p, "rb").read())).hexdigest()
r = {}
cl = load("catalogue/claims.json"); old = json.loads(git_show("catalogue/claims.json"))
assert len(cl["claims"]) == 365 and cl["claims"][:360] == old["claims"]
assert [c["status"] for c in cl["claims"][360:]] == ["PROGRAMME_PROVED"] * 4 + ["COMPUTED_EXACT"]
r["claims"] = "365; first 360 identical to entry"
assert load("catalogue/sources.json") == json.loads(git_show("catalogue/sources.json"))
r["sources"] = "unchanged"
for p in ("frontier/frontier.json", "tools/zsf/checker_a.py", "tools/zsf/checker_b.py"):
    assert lf(open(p, "rb").read()) == lf(git_show(p)), p
pf = load("sessions/S109/PREFLIGHT_SUMMARY.json")
for cam, n in (("CAM-0006", 15), ("CAM-0007", 20)):
    d = load(f"campaigns/{cam}/PREREGISTRATION.json")
    assert d["status"] == "PREREGISTERED_NOT_ACTIVATED" and d["completeness_class"].startswith("EXHAUSTIVE")
    for p, h in d["code_sha256"].items():
        assert sha(p) == h == pf["code_sha256"][p], (cam, p)
    assert not os.path.exists(f"campaigns/{cam}/checkpoints")
r["prereg"] = "CAM-0006/0007 hashes match preflight code; not run"
for n in ("2", "3", "4", "5", "6", "7"):
    x = pf["runs"][n]
    assert x["max_length_A"] == x["max_length_B"] == 3 * int(n) - 3 and x["orbit_set_sha256_A"] == x["orbit_set_sha256_B"]
for n in ("10", "12"):
    x = pf["runs"][n]
    assert x["A"]["max_length"] == x["B"]["max_length"] == 3 * int(n) - 3 and x["A"]["at_or_above_threshold"] == x["B"]["at_or_above_threshold"] == 0
r["preflight"] = "PASS"
s = load("authoritative/STATE.json")
assert s["last_completed_session"] == "S109" and s["recommended_next_session"] == "S110"
assert s["counterexample_hunt_strategy"]["campaigns_preregistered"] == ["CAM-0006", "CAM-0007"] and s["counterexample_status"] == "NONE_CLAIMED"
assert os.listdir("candidates") == ["README.md"]
r["state"] = "consistent"
r["overall"] = "PASS"
print(json.dumps(r, indent=1))
