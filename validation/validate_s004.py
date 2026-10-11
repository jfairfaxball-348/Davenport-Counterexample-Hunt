#!/usr/bin/env python3
"""S004 administrative consistency checks. No mathematical search or source code execution."""
import argparse
import hashlib
import json
import platform
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "validation/S004_VALIDATION.json"
REVIEW = ROOT / "validation/S004_REVIEW.json"
CHECKS = []


def require(condition, label):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files_with_suffix(suffix):
    return sorted(p for p in ROOT.rglob("*" + suffix)
                  if not any(part.startswith(".") for part in p.relative_to(ROOT).parts))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write deterministic validation output")
    args = parser.parse_args()
    json_files = files_with_suffix(".json")
    parsed = {str(p.relative_to(ROOT)): json.loads(p.read_text()) for p in json_files}
    require(len(parsed) == len(json_files), "all_repository_json_parses")
    sources = parsed["catalogue/sources.json"]
    claims = parsed["catalogue/claims.json"]
    frontier = parsed["frontier/frontier.json"]
    state = parsed["authoritative/STATE.json"]
    entry = parsed["sessions/S004/ENTRY_REVIEW.json"]
    review = parsed["validation/S004_REVIEW.json"]
    src_ids = [x["id"] for x in sources["sources"]]
    clm_ids = [x["id"] for x in claims["claims"]]
    require(src_ids == [f"SRC-{i:04d}" for i in range(1, 25)], "24_unique_stable_source_ids")
    require(clm_ids == [f"CLM-{i:04d}" for i in range(1, 73)], "72_unique_stable_claim_ids")
    require(all(x["access"] in sources["access_enum"] for x in sources["sources"]), "source_access_enum")
    require(all(x["status"] in claims["status_enum"] for x in claims["claims"]), "claim_status_enum")
    require(all(x["status"] == "INHERITED_UNVERIFIED" for x in claims["claims"][:37]), "inherited_claims_remain_quarantined")
    require(not any(x["status"] in {"COMPUTED_EXACT", "FORMALLY_CERTIFIED"} for x in claims["claims"]), "no_computation_or_certificate_upgrade")
    require(all(set(x.get("source_ids", [])) <= set(src_ids) for x in claims["claims"]), "claim_source_references_resolve")

    text_files = files_with_suffix(".md") + json_files
    known = set(src_ids + clm_ids)
    for path in text_files:
        refs = set(re.findall(r"\b(?:SRC|CLM)-\d{4}\b", path.read_text()))
        if not refs <= known:
            raise AssertionError(f"Unknown reference in {path.relative_to(ROOT)}: {refs - known}")
    require(True, "all_markdown_json_source_claim_references_resolve")
    for name, records, prefix, fields in [
        ("catalogue/SOURCES.md", sources["sources"], "SRC", ["title", "notes", "url", "access", "accessed"]),
        ("catalogue/CLAIMS.md", claims["claims"], "CLM", ["statement", "notes", "origin", "status"]),
    ]:
        text = (ROOT / name).read_text()
        definitions = re.findall(rf"^## ({prefix}-\d{{4}}) —", text, re.M)
        require(definitions == [x["id"] for x in records], f"{prefix.lower()}_markdown_unique_definitions")
        require(all(str(x[k]) in text for x in records for k in fields), f"{prefix.lower()}_markdown_mirrors_fields")

    rows = frontier["rows"]
    require([r["n"] for r in rows] == list(range(1, 31)), "30_unique_ordered_frontier_rows")
    # This finite table is transcribed from the paper audit, not discovered by search.
    upper = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 45,
             46, 49, 52, 55, 59, 63, 64, 67, 70, 73, 76, 79, 83, 85, 90]
    interval_ns = {15, 20, 21, 28, 30}
    for r, hi in zip(rows, upper):
        n = r["n"]
        lo = 3 * n - 2
        expected_bound = str(lo) if lo == hi else f"{lo}..{hi}"
        assert (r["group"], r["d_star"], r["lower_bound"], r["upper_bound"], r["reported_bound"]) == (
            f"C_{n}^3", lo, lo, hi, expected_bound), f"frontier n={n}"
        assert r["provisional_status"] == ("SANDWICHED" if n in interval_ns else "SETTLED")
        assert set(r["evidence"]) <= known | {"TRIVIAL_GROUP"}
        if n in interval_ns:
            assert r["programme_certification"] == "PROGRAMME_DERIVED_INTERVAL_FROM_SOURCE_THEOREMS"
        elif n in {6, 10, 12, 14, 18, 22, 24, 26}:
            assert r["programme_certification"] == "SOURCE_STATED_HISTORICAL_THEOREM"
    require(True, "all_frontier_values_evidence_classes_and_references_match_paper_audit")
    require(upper[14] == 3 * upper[4] + 6 and upper[19] == 2 * upper[9] + 3
            and upper[20] == 3 * upper[6] + 6 and upper[27] == 2 * upper[13] + 3
            and upper[29] == 3 * upper[9] + 6, "five_interval_arithmetic_deductions")
    md_rows = [l for l in (ROOT / "frontier/FRONTIER.md").read_text().splitlines()
               if re.match(r"\| \d+ \|", l)]
    expected_rows = [f"| {r['n']} | {r['group']} | {r['d_star']} | {r['reported_bound']} | "
                     f"{r['provisional_status']} | {', '.join(r['evidence'])} |" for r in rows]
    require(md_rows == expected_rows, "frontier_markdown_json_exact_table_match")
    require(sum(r["provisional_status"] == "SETTLED" for r in rows) == 25, "25_exact_or_trivial_rows_5_intervals")

    require(state["phases"]["1"]["status"] == "IN_PROGRESS"
            and all(state["phases"][str(i)]["status"] == "NOT_STARTED" for i in (2, 3))
            and state["phases"]["0"]["status"] == "PASS"
            and state["phases"]["4"]["status"] == "OWNER_GATED", "phase_gate_state")
    require(state["last_completed_session"] == "S004" and state["recommended_next_session"] == "S005"
            and state["phase1_target_n"] is None and state["campaign_active"] is None
            and frontier["recommended_phase2_target"] is None, "session_and_no_target_state")
    gates = (ROOT / "docs/PHASE_GATE_LEDGER.md").read_text()
    require("| Phase 1 frontier | IN_PROGRESS | S004" in gates
            and "| Phase 2 tooling | NOT_STARTED" in gates
            and "| Phase 3 campaigns | NOT_STARTED" in gates, "gate_ledger_state_consistency")
    campaign = (ROOT / "campaigns/REGISTRY.md").read_text()
    require(re.findall(r"^## (CAM-\d{4})", campaign, re.M) == ["CAM-0001"]
            and "PROPOSED / NOT RUNNING" in campaign and "activation blocked; premise obsolete" in campaign,
            "single_proposed_campaign_activation_blocked")
    require(not (ROOT / "sessions/S005").exists(), "s005_not_executed")
    require(not any((ROOT / "candidates").glob("*.json")) and not any(ROOT.glob("campaigns/CAM-*/checkpoints/*")),
            "no_candidate_or_campaign_output")
    require(review["phase1"] == "IN_PROGRESS" and review["phase2"] == review["phase3"] == "NOT_STARTED"
            and review["cam_0001"] == "PROPOSED_NOT_RUNNING" and review["target_n"] is None
            and review["n6_interval"] == "16" and review["source_count"] == 24 and review["claim_count"] == 72,
            "review_gate_and_counts_consistency")
    require(all(review[k] == 0 for k in ["campaigns_executed", "candidates", "orbit_counts_computed", "solvers"])
            and not review["source_code_executed"] and not review["lean_executed"] and not review["ci_pass_claimed"],
            "review_scope_no_execution_flags")

    require(entry["entry_main"] == entry["git_ls_remote_main"] == entry["github_api_main"] == review["entry_main"],
            "entry_main_independent_agreement")
    require(len(entry["pull_requests"]) == 3
            and all(p["merged_at"] and p["state"] == "closed" for p in entry["pull_requests"]),
            "all_prior_prs_merged_no_open_pr_at_entry")
    require(entry["pull_requests"][0]["merge_sha"] == entry["entry_main"]
            and entry["pull_requests"][0]["head_sha"] == entry["s003_merge_parents"][1], "s003_reconciliation")
    require(entry["actions_workflows"]["total_count"] == entry["actions_runs"]["total_count"]
            == entry["main_check_runs"]["total_count"] == entry["actual_jobs"]["count"] == 0
            and not entry["ci_pass_claimed"], "observed_ci_absence_not_pass")

    manifest = parsed["sessions/S004/INPUT_MANIFEST.json"]
    require(digest(ROOT / manifest["file"]) == manifest["sha256"], "verbatim_visible_input_transcription_hash")
    require("not a hash of original chat transport bytes" in manifest["scope"], "input_hash_scope_honest")
    prompt = (ROOT / "authoritative/NEXT_SESSION_PROMPT.md").read_bytes()
    closeout = (ROOT / "sessions/S004/CLOSEOUT.md").read_bytes()
    start = b"<!-- S005_PROMPT_START -->\n"
    end = b"<!-- S005_PROMPT_END -->"
    require(closeout.count(start) == closeout.count(end) == 1
            and closeout.split(start)[1].split(end)[0] == prompt, "byte_identical_full_s005_handoff")
    require(prompt.startswith(b"S005 ") and b"UNEXECUTED" in prompt and b"STOP after S005." in prompt,
            "handoff_identity_and_stop")
    source_manifest = parsed["sessions/S004/SOURCE_MANIFEST.json"]
    require(all(a["source_id"] in known and re.fullmatch(r"[0-9a-f]{64}", a["sha256"])
                and a["bytes"] > 0 for a in source_manifest["artifacts"]), "source_manifest_references_hashes_sizes")
    require(len(source_manifest["yiu_source_archive_members"]) == 5, "yiu_archive_scope_recorded")
    require(not files_with_suffix(".pdf") and not files_with_suffix(".lean"), "no_committed_source_pdf_or_formalisation_files")

    # Exclude this output and the review containing its hash to avoid a circular hash claim.
    hashed_inputs = sorted(set(text_files + [Path(__file__).resolve()]) - {OUTPUT, REVIEW})
    result = {
        "session": "S004", "scope": "ADMINISTRATIVE_ONLY_NOT_MATHEMATICAL_CERTIFICATION",
        "result": "PASS", "python": platform.python_version(), "checks_passed": CHECKS,
        "json_file_count": len(json_files), "source_count": 24, "claim_count": 72, "frontier_rows": 30,
        "phase1": "IN_PROGRESS", "phase2": "NOT_STARTED", "phase3": "NOT_STARTED",
        "campaign": "PROPOSED_NOT_RUNNING_ACTIVATION_BLOCKED", "n6": "16",
        "input_sha256": {str(p.relative_to(ROOT)): digest(p) for p in hashed_inputs},
        "hash_exclusions": ["validation/S004_REVIEW.json", "validation/S004_VALIDATION.json"],
    }
    output = (json.dumps(result, indent=2, ensure_ascii=False) + "\n").encode()
    if args.write:
        OUTPUT.write_bytes(output)
    else:
        assert OUTPUT.read_bytes() == output, "Recorded validation output differs; regenerate and review"
        assert review["output_sha256"] == hashlib.sha256(output).hexdigest(), "Review output hash differs"
        assert review["validator_sha256"] == digest(Path(__file__).resolve()), "Review validator hash differs"
        assert review["validation_result"] == "PASS", "Review validation not complete"
    print(json.dumps({"result": "PASS", "checks": len(CHECKS), "json_files": len(json_files),
                      "output_sha256": hashlib.sha256(output).hexdigest(),
                      "scope": result["scope"]}, sort_keys=True))


if __name__ == "__main__":
    main()
