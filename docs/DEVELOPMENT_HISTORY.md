# Full experimental trajectory and failed hypotheses (source-verified)

See `paper/extended_manuscript.pdf`, especially Table 1 and Sections 3-4. This record intentionally distinguishes public-score milestones from unrelated local validation populations and logged attempts.

| Stage | Evidence and decision |
|---|---|
| Initial V2--V4 | Semantic and compact-instance models; around 0.31--0.32 public PQ; a 0.4135 result on just 20 local images was overly optimistic. |
| V5--V6 | Baseline/checkpoint provenance; avoid using opaque precomputed predictions as if they were new trained models. |
| V7 | Native tile research; earlier user-confirmed public 0.34 control. |
| V8 / V8.1 | Trained 13-epoch tile specialist; JSON tuples vs lists broke its cache reader and invalidated initial evaluation. |
| V9 | Multi-scale ridge LightGBM; selected older fallback yielded public 0.31. |
| V10--V11 | Quality-consensus and learned fragment repair; V10 public 0.33, confidence in a 0.34 V7 reference. |
| V12--V15 | Frozen reference recovery and OOF delta-PQ: one apparent gain used a wrong reconstructed control. Guard original hashes. |
| V16 | ResUNet/FPN/YOLO search: best local YOLO11m PQ 0.38993, but public ~0.33. |
| V17--V20 | Global/native solar-pretrained inference; previous-best public milestone documented at 0.36. |
| V22--V23 | Multiscale fusion + occupancy and seam selection; original notebook documents 0.37. |
| V24 | V24 quality/learned prompt refinement; notebook records 0.38 public. |
| V25 | Locked 69-feature ranker plus selective real refinement: exact 1,093-row CSV with public 0.39. |
| V26 | Real-error refinement / counterfactual selector; no confirmed stronger public result in attached assets. |
| V27 | FilamentFormer-Lite learned instance queries; trained but not promoted over 0.39. |
| V28 | High-res expert detector, novel-instance gate: +0.000323 local with conservative fusion, not promoted; 32/502 qualifying candidate examples. |
| V29 | Novelty-credit ranking and fragment pairs: +0.000798 local with mean rank, not promoted; 61/363 qualifying candidate examples. |
| V30 | Referred to in later project notes; full executed V30 result unavailable, so no numeric claim is made. |

## Why the public track was not monotonic

Conventional loss or patch mAP is not the competition's object-level PQ; native crops can generate truncated or overlapping instances; candidate false positives matter directly; and an incorrectly reconstructed baseline can manufacture apparent gains. These are methodological findings, not a post hoc claim that every version advanced the score.

## Third-party early reference

The first research exploration tested a publicly shared I079 handoff by another Kaggle participant. That publicly available implementation is not republished here due to unclear redistribution terms. Cite its original source instead, and do not claim its source or weights were developed by this team.
