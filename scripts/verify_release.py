#!/usr/bin/env python3
"""Verify exact historical public score artifact and required trained-model identities."""
import argparse,csv,hashlib,json,sys
from pathlib import Path

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(2**20),b''):h.update(chunk)
    return h.hexdigest()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--weights-dir',type=Path,default=Path('models'))
    parser.add_argument('--csv',type=Path,default=Path('submissions/V25_EXACT_PUBLIC_039.csv'))
    parser.add_argument('--require-all-weights',action='store_true')
    args=parser.parse_args()
    expected='ac470fbfa0e2ca5f2d8a654d6c6bbaf549dd8980d040963ed8ba4821dc9ac329'
    if not args.csv.exists():raise SystemExit('MISSING scored V25 reference CSV: '+str(args.csv))
    actual=digest(args.csv)
    if actual!=expected:raise SystemExit(f'Wrong V25 public CSV SHA {actual}; expected {expected}')
    with args.csv.open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==['filament_id','segmentation_rle'],reader.fieldnames
        rows=list(reader)
    assert len(rows)==1093,len(rows)
    assert len({r['filament_id'] for r in rows})==1093
    print('PASS: historical V25 scored CSV — SHA256/1093 rows/unique IDs')
    manifest=json.loads(Path(__file__).resolve().parents[1].joinpath('models/checkpoint_manifest.json').read_text())
    missing=[];wrong=[]
    for m in manifest:
        p=args.weights_dir/m['file']
        if not p.is_file():
            missing.append(m['file']);print('MISSING',m['file']);continue
        if p.stat().st_size!=m['size_bytes'] or digest(p)!=m['sha256']:
            wrong.append(m['file']);print('HASH/SIZE MISMATCH',m['file'])
        else:print('PASS',m['file'])
    print('Missing weights:',len(missing),'Mismatch:',len(wrong))
    if wrong or (missing and args.require_all_weights):sys.exit(2)
    if missing:print('INCOMPLETE RELEASE: attach exact model files before public reproducibility claim.')
if __name__=='__main__':main()
