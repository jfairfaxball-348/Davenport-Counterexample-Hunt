"""S110: aggregate CAM-0006/0007 shard outputs into RESULT.json files (administrative).
Run from repo root: python -I sessions/S110/aggregate_results.py"""
import hashlib, json, os

lf = lambda b: b.replace(b"\r\n", b"\n")
exits = {}
for line in open("sessions/S110/job_exits.txt", encoding="utf-8"):
    p = line.split()
    exits[(p[0], p[1], int(p[2]))] = dict(start=p[3][6:], end=p[4][4:], exit=int(p[5][5:]))
summary = {}
for cam, n, L in (("CAM-0006", 15, 43), ("CAM-0007", 20, 58)):
    pre = json.load(open(f"campaigns/{cam}/PREREGISTRATION.json", encoding="utf-8"))
    d = f"campaigns/{cam}/checkpoints"
    res = dict(campaign=cam, executed_in="S110", date="2026-10-17", n=n, target_length=L,
               completeness_class=pre["completeness_class"], code_sha256=pre["code_sha256"],
               python="3.12.10", numpy="1.26.4", algorithms={})
    complete = True
    for alg in ("a", "b"):
        exp = pre["algorithms"][alg.upper()]["expected_pairs_total"]
        shards, hist, logs = [], {}, {}
        for k in range(14):
            e = exits.get((cam, alg, k))
            out = f"{d}/{alg}-s{k}.json"
            r = json.load(open(out)) if os.path.exists(out) else None
            jl = f"{d}/{alg}-s{k}.jsonl"
            raw = open(jl, "rb").read()
            recs = [json.loads(x) for x in lf(raw).decode().splitlines() if x.strip()]
            hits = [x for x in recs if x["kind"] == "AT_OR_ABOVE"]
            ended = bool(recs) and recs[-1]["kind"] == "end"
            logs[f"{alg}-s{k}.jsonl"] = dict(sha256_lf=hashlib.sha256(lf(raw)).hexdigest(), bytes_lf=len(lf(raw)))
            st = "COMPLETE" if (e and e["exit"] == 0 and r and ended) else ("WALLTIME_CAP_TRUNCATED" if e and e["exit"] == 124 else "INCOMPLETE")
            if st != "COMPLETE":
                complete = False
            shards.append(dict(shard=k, status=st, exit=e["exit"] if e else None, start=e["start"] if e else None, end=e["end"] if e else None,
                               pairs_evaluated=r["pairs_evaluated"] if r else None, max_length=r["max_length"] if r else None,
                               seconds=r["seconds"] if r else None, at_or_above_records=len(hits)))
            if r:
                for kk, v in r["histogram"].items():
                    hist[kk] = hist.get(kk, 0) + v
        tot = sum(s["pairs_evaluated"] or 0 for s in shards)
        if tot != exp:
            complete = False
        res["algorithms"][alg.upper()] = dict(code=pre["algorithms"][alg.upper()]["code"], expected_pairs_total=exp, pairs_evaluated_total=tot,
                                             coverage_full=tot == exp, max_optimum=max(s["max_length"] or -1 for s in shards),
                                             at_or_above_threshold=sum(s["at_or_above_records"] for s in shards),
                                             histogram_of_optima=dict(sorted(hist.items(), key=lambda x: int(x[0]))),
                                             cpu_seconds_sum=round(sum(s["seconds"] or 0 for s in shards), 1), shards=shards, log_sha256=logs)
    A, B = res["algorithms"]["A"], res["algorithms"]["B"]
    agree = A["max_optimum"] == B["max_optimum"] and set(A["histogram_of_optima"]) == set(B["histogram_of_optima"]) and A["at_or_above_threshold"] == B["at_or_above_threshold"]
    res["two_algorithm_agreement"] = agree
    if complete and agree and A["max_optimum"] <= L - 1 and A["at_or_above_threshold"] == 0:
        res["campaign_status"] = "COMPLETED_EXHAUSTIVE_NO_HIT"
        res["result"] = f"No zero-sumfree sequence over C_{n}^3 with at most five distinct values has length {L} (= 3n-2); the maximum is {A['max_optimum']} = 3n-3. Scope: support-<=5 family only; NOT SAT{n}, not a D value. Certificate: two independent exhaustive algorithms with full coverage + committed shard logs (no Lean/DRAT)."
    elif not agree:
        res["campaign_status"] = "BLOCKER_ALGORITHM_DISAGREEMENT"
    elif A["at_or_above_threshold"] or B["at_or_above_threshold"]:
        res["campaign_status"] = "TARGET_REACHED_CANDIDATE_PENDING"
    else:
        res["campaign_status"] = "PARTIAL_NO_CLAIM"
    open(f"campaigns/{cam}/RESULT.json", "w", newline="\n").write(json.dumps(res, indent=1) + "\n")
    summary[cam] = dict(status=res["campaign_status"], A=(A["pairs_evaluated_total"], A["expected_pairs_total"], A["max_optimum"], A["at_or_above_threshold"]),
                        B=(B["pairs_evaluated_total"], B["expected_pairs_total"], B["max_optimum"], B["at_or_above_threshold"]), agree=agree)
print(json.dumps(summary, indent=1))
