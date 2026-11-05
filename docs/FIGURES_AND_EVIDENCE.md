# Figure and table source map

**Original frozen V25 audit (51 scenes, 46 days; actual exported evidence):**
- `Fig00_frozen_V25_pipeline_schematic` — procedural architecture diagram; actual component sequence, not a screenshot.
- `Fig01_V25_component_ablation_PQ` — 12 true frozen model interventions with shared scorer/population.
- `Fig02_component_PQ_deltas_CI` — 2,000 descriptive paired acquisition-day bootstrap replicates.
- `Fig03_V25_instance_size_recall` and `Fig04_expert_agreement` — size and expert-annotation analyses.
- `Fig05_retrained_ranker_feature_ablation` and `Fig06_ranker_reliability` — 3 seeds for ranker refits; no full model-seed replication.
- `Fig07_case_01..08` — eight true labeled H-alpha images with three actual model variants. Red/yellow/green indicate pixel mismatch/overlap, not one-to-one instance TP/FP labels.

**Archival historical syntheses:**
- `Fig00_development_milestones` — selected public-score references found in notebook history. They are from different scored recipes and cannot be read as held-out model-training points.
- `Fig00_failures_matrix` — descriptive taxonomy of historical attempts, not a numeric validation.

**Separate V28/V29 report-log comparison:**
- `Fig11_qualifying_novelty_candidates_log` and `Fig12_v28_v29_completed_log_audit_comparison` — completion log transcription, not independent reanalysis of per-scene predictions; candidate banks not matched.

**Separate earlier 105-scene detector evidence run:**
- `Fig05_selected_area_recall`, `Fig10_fragmentation_diagnostic`, `Fig07_learning_00` — useful for historical diagnosis; **must not be mixed with the 51-scene final ablation table**.
