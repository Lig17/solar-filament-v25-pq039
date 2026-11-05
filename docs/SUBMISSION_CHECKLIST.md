# Competition final-submission check

The official competition announces a November 15, 2026 deadline and requires a four-page report in the organizer's ACM-like Overleaf template, a publicly accessible repository, `requirements.txt`, model weights, a runnable pipeline notebook, and Google Form completion. Confirm the currently displayed deadlines and portal details immediately before submission.

- [ ] Read the competition's official Final Submission and Open Access rules.
- [ ] Upload all seven exact trained model files, verify SHA256, and prove they are publicly downloadable.
- [ ] Run the `01_reconstruct_and_verify_v25_submission.ipynb` notebook on all 180 test images, and inspect its comparison report.
- [ ] Run `scripts/verify_release.py --require-all-weights` from repo root with the correct model path.
- [ ] Confirm `V25_EXACT_PUBLIC_039.csv` reproduces the selected Kaggle score, or choose the actual correct scored CSV and update the manuscript truthfully.
- [ ] Verify `paper/competition_4page/main.pdf` is four pages, has the intended authors, the organizer's acknowledgments and actual references.
- [ ] Publish the GitHub repo; a ZIP attachment alone is not a live accessible repo.
- [ ] Ensure Git LFS checkout is supported and weight links do not require team-member approval.
- [ ] Complete organizer's Google Form, paste public repo URL, upload report PDF, and retain confirmation.
- [ ] Avoid treating a workshop submission as equivalent to the competition form. Workshop review is separate.
