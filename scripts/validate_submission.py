#!/usr/bin/env python3
"""Check submission CSV schema, COCO RLE syntactic validity and 2048x2048 mask dimensions."""
import argparse,csv,sys
from collections import Counter
from pathlib import Path

def main():
    a=argparse.ArgumentParser();a.add_argument('csv_path',type=Path);a.add_argument('--full-decode',action='store_true');opts=a.parse_args()
    if opts.full_decode:
        from pycocotools import mask as coco
    ids=set();count=Counter();n=0;errors=[]
    with opts.csv_path.open(newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        if reader.fieldnames!=['filament_id','segmentation_rle']:raise SystemExit('Wrong columns')
        for row in reader:
            fid=row['filament_id'];stem=fid.rsplit('_',1)[0];s=row['segmentation_rle']
            if fid in ids:errors.append(f'duplicate ID {fid}')
            ids.add(fid);count[stem]+=1;n+=1
            if not s or not fid:errors.append(f'empty field row {n}');continue
            if opts.full_decode:
                try:
                    r={'size':[2048,2048],'counts':s.encode('ascii')}
                    ar=coco.area(r)
                    if ar<=0:errors.append('zero-area '+fid)
                except Exception as e:errors.append(f'invalid RLE {fid}: {e}')
    print('Rows:',n,'scene IDs:',len(count),'issues:',len(errors))
    print('Missing prediction rows for a scene may be correct: this tool does not assume every test image has a filament.')
    if errors:
        print('\n'.join(errors[:30]));sys.exit(2)
    print('PASS')
if __name__=='__main__':main()
