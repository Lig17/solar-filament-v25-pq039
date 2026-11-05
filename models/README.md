# Original V25 trained model assets — REQUIRED before final GitHub publication

The dataset and completed evidence archive supplied to this chat contain **model hashes and summaries, but not these original checkpoint bytes**. It would be incorrect to claim the ZIP alone provides turnkey inferencing.

Acquire the following **original byte-identical** files from your own saved Kaggle outputs (`solarouts` and `v25ftss`) and place them in this folder (or provide verified accessible Git-LFS / release links):

| Model asset | Type | Approx. size |
|---|---|---|
| `portable_global_m_best.pt` | V20 global YOLO11m | 45.4 MB |
| `portable_native_m_best.pt` | V20 native YOLO11m | 45.2 MB |
| `SOLAR_V24_REFINER_BEST.pt` | V24 prompt refiner | 55.1 MB |
| `SOLAR_V24_INSTANCE_QUALITY.joblib` | V24 15-feature ranker | 0.16 MB |
| `SOLAR_V25_CURVE_BEST.pt` | V25 curve network | 4.0 MB |
| `SOLAR_V25_REAL_REFINER_BEST.pt` | V25 real-mask refiner | 55.1 MB |
| `SOLAR_V25_EXTENDED_QUALITY.joblib` | V25 69-feature rank ensemble | 3.2 MB |

All exact SHA-256 hashes and sizes are recorded in [`checkpoint_manifest.json`](checkpoint_manifest.json). Run `python scripts/verify_release.py --weights-dir models --require-all-weights` from the repository root. **No substitute models or random pretrained weights are acceptable.**

For GitHub, use Git LFS and make files truly fetchable by the judges. If the terms of your saved model training permit public release, store the checkpoint files themselves. Do not link to private Kaggle output datasets that require login permissions absent from the judges.
