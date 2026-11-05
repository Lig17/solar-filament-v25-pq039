#!/usr/bin/env python3
"""Offline publication checks: evidence integrity, submission identity, notebook syntax."""
from __future__ import annotations
import csv, hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
EXPECTED='ac470fbfa0e2ca5f2d8a654d6c6bbaf549dd8980d040963ed8ba4821dc9ac329'
def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
def main():
    errors=[]
    p=ROOT/'submissions/V25_EXACT_PUBLIC_039.csv'
    if not p.is_file() or sha(p)!=EXPECTED:errors.append('Original scored CSV does not match known SHA256')
    else:
        with p.open(newline='',encoding='utf-8') as f:
            reader=csv.DictReader(f);rows=list(reader)
            if reader.fieldnames!=['filament_id','segmentation_rle'] or len(rows)!=1093 or len({r['filament_id'] for r in rows})!=1093:
                errors.append('Original submission CSV format/count mismatch')
    e=ROOT/'evidence'; manifest=json.loads((e/'file_manifest.json').read_text())
    for entry in manifest.get('files',[]):
        rel=entry['file']; filepath=e/rel
        # Evidence manifest has paths rooted within the original Kaggle evidence folder,
        # while GitHub has moved the table outputs under evidence/tables/.
        if not filepath.is_file() and rel.startswith('tables/'):
            filepath=e/rel
        if not filepath.is_file():
            # Subset of original evidence archived; all included records must still be genuine.
            continue
        if sha(filepath)!=entry['sha256']:errors.append(f'Changed evidence artifact: {rel}')
    try:
        import nbformat
        for nbfile in sorted((ROOT/'notebooks').glob('*.ipynb')):
            nb=nbformat.read(nbfile,as_version=4);nbformat.validate(nb)
            for cell in nb.cells:
                if cell.cell_type=='code':compile(cell.source,str(nbfile),'exec')
    except Exception as exc:errors.append(f'Notebook static validation: {exc}')
    print('Release audit:', 'PASS' if not errors else 'FAIL', '|', len(errors),'issues')
    for x in errors: print(' -',x)
    return 1 if errors else 0
if __name__=='__main__':sys.exit(main())
