# Integration review correction

The first P4 implementation and settled test passed, but hostile review found that preliminary candidate JSON was written in the shard output directory. Repository rule 5 requires candidates to stay in candidates/. Before any target activation, route exports through the specification's candidate_directory; CAM-0008 pins candidates/CAM-0008. Settled fixtures use an isolated temporary directory and are not target candidates.

Original runtime/test/output are preserved in revisions/ and match INTEGRATION_MANIFEST.json. Final files are frozen under INTEGRATION_MANIFEST_V2.json and the full settled integration suite is rerun. P1/P2/P3 code and outputs are unchanged. This is a governance/output-routing repair, not a change to either mathematical predicate. No target pair was evaluated in either version.
