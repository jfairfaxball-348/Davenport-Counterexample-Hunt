#!/usr/bin/env bash
# S110 orchestrator for CAM-0006 / CAM-0007 exactly as pre-registered (S109):
# 14 shards per algorithm, timeout 43200 s per shard, at most 14 concurrent processes,
# order: CAM-0006 A+B, then CAM-0007 B, then CAM-0007 A.
cd "$(dirname "$0")/../.."
mkdir -p campaigns/CAM-0006/checkpoints campaigns/CAM-0007/checkpoints
JOBS=sessions/S110/jobs.txt
: > "$JOBS"
for alg in a b; do for k in $(seq 0 13); do echo "CAM-0006 15 43 $alg $k" >> "$JOBS"; done; done
for k in $(seq 0 13); do echo "CAM-0007 20 58 b $k" >> "$JOBS"; done
for k in $(seq 0 13); do echo "CAM-0007 20 58 a $k" >> "$JOBS"; done
date -u +%FT%TZ > sessions/S110/activation_utc.txt
run_one() {
  set -- $1
  cam=$1; n=$2; L=$3; alg=$4; k=$5
  d=campaigns/$cam/checkpoints
  start=$(date -u +%FT%TZ)
  timeout 43200 python -I tools/zsf/support5_$alg.py --n $n --threshold $L --report-keys-at $L \
      --shard $k --nshards 14 --checkpoint $d/$alg-s$k.jsonl --out $d/$alg-s$k.json > /dev/null 2> $d/$alg-s$k.err
  rc=$?
  echo "$cam $alg $k start=$start end=$(date -u +%FT%TZ) exit=$rc" >> sessions/S110/job_exits.txt
}
export -f run_one
xargs -a "$JOBS" -I{} -P 14 bash -c 'run_one "$@"' _ {}
date -u +%FT%TZ >> sessions/S110/activation_utc.txt
echo ALLDONE
