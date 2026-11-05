# MAGFiLO Final Paper Evidence — V25 verified 0.39 public submission

## Evidence authority
- Historical Kaggle public PQ: **0.39**, user-confirmed for original V25 CSV only.
- Historical CSV SHA256: `ac470fbfa0e2ca5f2d8a654d6c6bbaf549dd8980d040963ed8ba4821dc9ac329`; rows: `1093`.
- Frozen V25 reconstruction local audit PQ: **0.458880** (historically reused CAL/AUDIT; NOT Kaggle public PQ).
- Local audit = 51 scenes, 46 acquisition days. Historical calibration = 53 scenes.
- Full pipeline has 2 frozen YOLO11m-seg sources (global 1792px and native 1280 crops), V24 15-feature quality context/refiner, curve candidate U-Net, V25 69-feature ranker (cutoff .38), V25 real-mask refiner.

## Experimental reports
- `tables/Table01_same_scene_component_ablation.csv`: actual component-removal/addition results on identical scenes.
- `tables/Table02_paired_day_bootstrap.csv`: descriptive date-cluster confidence intervals; do not treat as independent-test p-values.
- `tables/Table03_inter_annotator_agreement.csv`: expert versions and agreement; do not call it an upper bound.
- `tables/Table04_instance_size_recall.csv`: per-instance recall by ground-truth size.
- `tables/Table05_overlap_multiplicity.csv`: split/merge heuristics, not physically verified structure claims.
- `tables/Table06_retrained_feature_group_ablation.csv`: separate quality-ranker fitting; seeds: (2026, 2037, 2048).
- `figures/Fig07_case_*`: genuine annotated solar-disk images, detector vs ranker vs full reconstructed masks.
- `tables/Table08_reconstructed_to_historical_public_agreement.csv`: optional comparison to exact scored CSV; mode executed: False.

## Mandatory limitations for manuscript
1. The 104 V20 detector-holdout images have been repeatedly inspected/tuned in V20–V29. The 53/51 split is **not** independent of prior method development.
2. The local pooled PQ scorer is the historical proxy; its parity with the official competition evaluator has not been verified.
3. Training seeds for frozen V20/V24/V25 convolutional backbones are NOT replicated by this notebook. The ranker seed study is NOT full multi-seed network replication.
4. Ablations are intervention-at-inference on already-trained components. They estimate removal effects; full retraining-without-component is a distinct, more expensive causal question.
5. V25 curve masks are not directly accepted by the historical winning decoder; curve candidates can influence ranker neighborhood/context. Explicit `V25_add_curve_candidates` is an experimental alternative, not part of the proven scored pipeline.
6. No claims of V26–V30 public improvements are made. Those experimental methods never supersede the original 0.39 score here.
7. Multi-annotator physical PQ aggregation and macro-Dice must be checked against the organizer's evaluator before submission.
8. Competition report and high-tier independent research paper have different evidential requirements. This notebook serves the former and core experimental analysis for the latter.
