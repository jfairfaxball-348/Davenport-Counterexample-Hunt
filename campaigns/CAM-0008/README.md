# CAM-0008 — registered, not executed

Single n15 profile (3,8,8,8,8,8), 5,815,950 covering pairs. Activation S117 or later, only after the S116 tooling gate is committed and a later owner invocation. All scope, code/input hashes, shards and caps are in PREREGISTRATION.json. Read research/S116_PAIR_ENGINE_TOOLING.md first.

Use one process at a time. Check disk space (3 GiB output allowance), no conflicting shard writer, pinned environment/code/input hashes, session deadline and cumulative campaign ledger. The runtime checks pins; the session operator enforces aggregate budgets and global stop rules. A per-process cap is not a substitute for the session deadline.

Controlled bootstrap for the first registered shard, AFTER activation:

    python -X utf8 -c "import sys,runpy; sys.path.insert(0,'tools/zsf'); runpy.run_path('tools/zsf/pair_campaign.py',run_name='__main__')" campaigns/CAM-0008/PREREGISTRATION.json campaigns/CAM-0008/output --engine a --shard 0 --seconds 21600

The explicit module path supports sibling imports. Do not run the script with isolated mode alone, which removes its directory from sys.path. Pass the remaining session budget, capped by the specification. Start with matched A/B jobs on shards 0 and 72. Record external elapsed times, exit/status and exact completed intervals. The registered 2x slower-observed-rate projection must fit the remaining 36 CPU-hour engine cap before more shards; otherwise stop for review. Never widen scope or silently change hashes.

Resume the identical spec/engine/shard/output directory. Never remove a committed failed/corrupt chunk to continue. On a candidate, stop all campaign work; the preliminary sequence goes under candidates/CAM-0008 and needs independent checking, Lean verification and a later-session cold check. A disagreement or exception also stops the campaign.

After both engines complete every shard, use the same bootstrap with `--audit`, within its separate six-hour budget. Save complete output and hashes. Audit checks every ordinal, A/B outcome, admissibility and every zero witness. Only full completion supports this one-profile exclusion. A timed-out audit, partial campaign or missing record supports none. No execution or exclusion is claimed at registration.
