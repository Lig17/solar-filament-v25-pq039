#!/usr/bin/env bash
# Safe, transparent GitHub publication of the V25 competition release.
set -euo pipefail
cd "$(dirname "$0")"
REPO="${GITHUB_REPO:-Lig17/solar-filament-v25-pq039}"
MODE="${1:-complete}"
if [[ "$MODE" != 'complete' && "$MODE" != '--source-only' ]]; then
  echo 'Usage: bash publish_to_github.sh [complete|--source-only]' >&2
  exit 2
fi
for cmd in python git gh; do
  command -v "$cmd" >/dev/null || { echo "Missing $cmd. Install it first." >&2; exit 2; }
done
if [[ "$MODE" == complete ]]; then
  command -v git-lfs >/dev/null || git lfs version >/dev/null 2>&1 || {
    echo 'Git LFS is required to upload original model checkpoint files.' >&2; exit 2;
  }
  python scripts/verify_release.py --weights-dir models --require-all-weights
else
  python scripts/verify_release.py --weights-dir models
  echo 'WARNING: SOURCE ONLY. Missing checkpoint files make the release INCOMPLETE for competition judging.'
fi
python scripts/audit_release.py
# Keep the operation idempotent and avoid overwriting an existing user's repository.
gh auth status >/dev/null
if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository $REPO already exists. Nothing pushed; inspect it before merging." >&2
  exit 3
fi
if [[ -d .git ]]; then
  echo 'This directory is already a git repository. Aborting automatic initialization.' >&2
  exit 3
fi
git init -b main
if [[ "$MODE" == complete ]]; then git lfs install --local; fi
# Uses the current user's git config for actual commit attribution.
git var GIT_AUTHOR_IDENT >/dev/null
git add .
git commit -m "Release V25 solar filament segmentation research and reproducibility artifacts"
gh repo create "$REPO" --public --source=. --remote=origin --push
printf '\nRepository created: https://github.com/%s\n' "$REPO"
if [[ "$MODE" == '--source-only' ]]; then
  echo 'DO NOT submit this incomplete repository as the competition reproducibility requirement.'
else
  echo 'Publish complete. Recheck that LFS model assets are publicly downloadable without credentials.'
fi
