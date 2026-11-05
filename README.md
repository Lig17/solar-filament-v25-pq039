# Solar Filament Segmentation Challenge 2026 — V25 Quality-Aware Multiscale Instance Segmentation

**Publication status:** [RELEASE_STATUS.md](RELEASE_STATUS.md) — checkpoint assets missing; source-only until complete reproduction is verified.


**Competition artifact:** V25 original scored submission, **Kaggle public PQ 0.39 (rounded; user-confirmed)**.

**Research focus:** Multi-scale solar filament instance detection, learned quality-aware selection, and selective prompt-conditioned mask refinement on GONG H-alpha images. The accompanying 22-page research manuscript gives a complete chronology of hypotheses, setbacks, unsuccessful alternatives, the frozen V25 model, fixed-checkpoint ablations, reliability and morphology analyses, and later V28/V29 negative findings.

**Important disclosure:** This ZIP contains all available manuscript source, original scored CSV, evidence metrics, figures, provenance manifests, and original/cleaned experiment notebooks, **but it does not contain the seven original trained-model weights**. Those must be added from your Kaggle outputs before this repository satisfies the competition's fully reproducible-model requirement. No evidence here claims that the team has won or that an independent new-test score was measured.

## Most important results

| Dataset/measurement | Result | Evidence status |
|---|---:|---|
| Kaggle public score | **0.39** | User-confirmed historical V25 file, rounded |
| Original scored CSV | 1,093 masks | Full exact SHA-256 checked |
| V25 reconstructed, 51 historical audit scenes | 0.458880 local PQ | Recomputed from frozen model outputs in final ablation notebook |
| Without quality ranker | 0.448975 local PQ | Same historical audit |
| Without real-mask refiner | 0.446886 local PQ | Same historical audit |
| Without both-detector fusion | 0.436862 local PQ | Same historical audit |
| V28/V29 best later alternatives | +0.000323 / +0.000798 local PQ | Historical execution logs, **not** publicly promoted |

The 51-scene audit was repeatedly consulted in previous development. Reported bootstrap intervals are descriptive, not new-sample hypothesis tests. Organizer scoring parity remains unverified.

## Repository structure

```text
paper/
  extended_manuscript.pdf          # Full chronological technical manuscript (22 pages)
  extended_manuscript.tex          # Editable LaTeX
  competition_4page/              # Four-page original-template ACM technical report + source
  figures/                        # Source images and PDFs used by the extended manuscript
notebooks/
  01_reconstruct_and_verify_v25_submission.ipynb  # Test inference only; full 180-image comparison
  02_final_v25_component_ablations.ipynb          # 12 frozen component ablations + 3-seed rankers
history/                          # Curated original source notebooks V4 through V29
models/
  checkpoint_manifest.json        # Seven exact original model hashes
  README.md                       # Where/how to attach missing original model weights
submissions/
  V25_EXACT_PUBLIC_039.csv         # Historical scored CSV, exact bytes — DO NOT MUTATE
scripts/
  verify_release.py               # SHA checks, provenance gate
  validate_submission.py          # Schema + optional RLE decode check
  compare_submissions.py          # Same-image RLE matching diagnostic
figures/                          # Presentation-quality figures
 evidence/                        # Original exact CSV, per-scene metrics, figures' data and provenance
requirements.txt                  # Executed Kaggle package-version baseline
```

## Running the exact V25 experiment on Kaggle

1. Upload these files to a public GitHub repository and **add seven original model files** (see `models/README.md`). If weights exceed normal Git guidance, use Git LFS with accessible downloads. GitHub and this chat do not automatically install those weights.
2. Use Kaggle GPU T4/T4x2, and attach the official competition `solar3k` dataset. Attach your V20/V24/V25 checkpoint dataset(s) or extract the original model files into a Kaggle input dataset. Enable Internet if Kaggle lacks `ultralytics==8.4.189` or `pycocotools`.
3. Run `notebooks/01_reconstruct_and_verify_v25_submission.ipynb`. It checks trained weight SHA prefixes, predicts all 180 unlabeled test images, writes a **new unscored** reconstructed CSV, and compares each scene to the original scored artifact if the original CSV is attached.
4. If outputs differ, investigate software-version parity, serialization, confidence gates, and postprocessing. Do **not** present the new CSV as the 0.39 scoring output. Retain the original artifact with SHA `ac470fbfa0e2ca5f2d...`.
5. Run `notebooks/02_final_v25_component_ablations.ipynb` with the training annotations and original checkpoints to regenerate the paper tables/figures. This is exploratory historical-audit evidence, **not** the hidden test score.
6. Verify the complete release:

```bash
python scripts/verify_release.py --weights-dir models --require-all-weights
python scripts/validate_submission.py submissions/V25_EXACT_PUBLIC_039.csv --full-decode
```

The inference notebook uses the previously tested experimental code and checks. It was statically validated when packaged, **but not rerun on GPU in this file-build environment**. Execute once on Kaggle and compare its output before asserting complete reproducibility.

## Which document goes where?

- **Kaggle Google Form:** upload `paper/competition_4page/main.pdf` (four pages, as requested in the supplied challenge template) and the **public GitHub repository URL**. Confirm the correct Kaggle final CSV is selected. The organizer requires source and model weights; this ZIP must be supplemented.
- **Extended paper or future research submission:** use `paper/extended_manuscript.pdf` as a detailed technical record, adapting formatting, novelty claims, and fresh-test experiments to the target venue. It is not a substitute for the challenge's four-page report.
- **Method provenance:** `history/` preserves the sequential alternative experiments, including failures, not a collection of claims that each version improved scores.

## Data provenance and copyright

The benchmark is MAGFiLO v1.0, originally described by Ahmadzadeh et al., *Scientific Data* (2024), DOI `10.1038/s41597-024-03876-y`, and distributed through the permitted 2026 competition. No external annotated versions of the 180 hidden-label test scenes are included. Original data must be downloaded through the organizer's platform under its terms.

Some initial research notebooks examined a public competitor's I079 handoff. The actual third-party implementation from that early investigation is **not redistributed** by this repository; see `docs/DEVELOPMENT_HISTORY.md`. The scripts newly authored for release use the MIT license. All historical notebook code remains subject to its original applicable terms and any third-party attributions.

## Claim limits

- The 0.39 public value is rounded and known only for the immutable original file, not regenerated predictions.
- The original validation split was reused across V20--V29: descriptive local uncertainty is not independent generalization confidence.
- Original YOLO/refiner training seeds have not been independently repeated here. Only ranker feature-family refits have three seeds.
- The local evaluator is a historical proxy; check the organizer's official self-evaluation notebook for matching and edge-case behavior.
- The V25 curve candidate generator contributes optional/contextual signals; **directly adding curve candidates reduced** local PQ in ablations.
- The original trained model files must be added to enable end-to-end reproduction from images.

## Sources

- [Competition overview and rules](https://www.kaggle.com/competitions/filament-segmentation-2026)
- [MAGFiLO Scientific Data paper](https://doi.org/10.1038/s41597-024-03876-y)
- [Panoptic Segmentation (Kirillov et al., CVPR 2019)](https://doi.org/10.1109/CVPR.2019.00963)
