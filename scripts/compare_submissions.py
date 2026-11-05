#!/usr/bin/env python3
"""Compare reconstructed masks with immutable V25 scored masks per image without accessing GT."""
from pathlib import Path
from collections import defaultdict
import argparse,pandas as pd,numpy as np
from scipy.optimize import linear_sum_assignment
from pycocotools import mask as coco

def parse(path):
    df=pd.read_csv(path,dtype=str);assert list(df)==['filament_id','segmentation_rle']
    groups=defaultdict(list)
    for r in df.itertuples(index=False):groups[r.filament_id.rsplit('_',1)[0]].append({'size':[2048,2048],'counts':r.segmentation_rle.encode('ascii')})
    return groups

a=argparse.ArgumentParser();a.add_argument('reference_csv',type=Path);a.add_argument('reconstructed_csv',type=Path);a.add_argument('--output',type=Path,default=Path('reproduction_comparison.csv'));opts=a.parse_args()
ref=parse(opts.reference_csv);test=parse(opts.reconstructed_csv)
rows=[]
for stem in sorted(set(ref)|set(test)):
    g=ref.get(stem,[]);p=test.get(stem,[])
    arr=np.asarray(coco.iou(g,p,[0]*len(p)),float) if g and p else np.zeros((len(g),len(p)))
    if arr.size:
        i,j=linear_sum_assignment(-arr);val=arr[i,j];match=int((val>.999).sum());avg=float(val.mean())
    else:match=0;avg=float('nan')
    rows.append(dict(stem=stem,reference=len(g),reconstructed=len(p),near_identical=match,mean_assignment_iou=avg,all_near_identical=match==len(g)==len(p)))
df=pd.DataFrame(rows);df.to_csv(opts.output,index=False)
print('Compared scenes:',len(df),'nonmatching scenes:',int((~df.all_near_identical).sum()))
if not df.all_near_identical.all():
    print('NOT REPRODUCED: Do not claim the reconstructed file was the scored 0.39 CSV.')
