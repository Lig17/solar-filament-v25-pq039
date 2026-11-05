# Release status — November 2, 2026

This repository is a documented **source-only research release**, not yet a complete competition-ready GitHub submission.

- Verified original V25 competition submission: `submissions/V25_EXACT_PUBLIC_039.csv` (SHA-256 `ac470fbfa0e2ca5f2d8a654d6c6bbaf549dd8980d040963ed8ba4821dc9ac329`, 1,093 instances). Historical public PQ **0.39**, rounded and user-reported.
- Reproduced historical-audit study: 51 annotated scenes, 46 acquisition days, reconstructed V25 local proxy PQ **0.458880**. This local estimate is *not* the public leaderboard score and not an untouched holdout.
- Manuscripts: the four-page competition report and the longer research record are included under `paper/`.
- Model availability: **all seven original checkpoint files still need to be added**; see `models/checkpoint_manifest.json`. The 180-test-image full reconstruction and original-CSV agreement were **not run** in the final evidence experiment.
- The official evaluator equivalence has not been established. Do not claim exact end-to-end reproduction until Kaggle regeneration and matching are verified.

## Publish as complete repository (recommended)

From a Linux system with the [GitHub CLI](https://cli.github.com/) and [Git LFS](https://git-lfs.com/) installed:

1. Obtain all seven **original** model files listed in `models/README.md` and place them in `models/`.
2. Run `python scripts/verify_release.py --weights-dir models --require-all-weights`. Resolve every hash mismatch.
3. Run the `notebooks/01_reconstruct_and_verify_v25_submission.ipynb` on Kaggle with original model assets and compare masks for all 180 images against the exact scored file. Investigate any discrepancies.
4. Authenticate GitHub CLI: `gh auth login`. Set actual Git author info (`git config --global user.name ...` and `git config --global user.email ...`).
5. Run `bash publish_to_github.sh complete`. Default new repository name: `Lig17/solar-filament-v25-pq039`. This **creates a new public repository** only if it does not exist; it never overwrites an existing repository.
6. Confirm the `.pt` and `.joblib` Git LFS pointers download correctly for a reader without your personal credentials. Verify the notebook works with *publicly available* weights.
7. Complete the competition Google Form with the four-page report PDF, final Kaggle prediction selection and **public** GitHub URL before the organizer's deadline.

## Publish sources early, but incomplete

If needed, `bash publish_to_github.sh --source-only` creates a public code-and-evidence repository **without the model weights** and prints an explicit warning. Do not claim it satisfies the competition's reproducibility rule. Once models are available, commit and push them using Git LFS.

## To avoid accidental disclosure

Check notebooks and historical experiments for private paths, hardcoded credentials, personal data, or third-party code rights before making the repository public. The scripts do **not** alter historical records or submit anything to Kaggle/Google Forms.
