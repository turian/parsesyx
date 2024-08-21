#!/usr/bin/env python3

import json
from collections import Counter, defaultdict

from tqdm import tqdm

key_values = defaultdict(list)

for l in tqdm(open("main.json")):
    o = json.loads(l)
    if o:
        for k, v in o.items():
            key_values[k].append(v)

for k in key_values:
    if k.startswith("NAME CHAR"):
        continue
    c = Counter(key_values[k])
    # print({k: [(v, c[v]) for v in sorted(set(key_values[k]))]})
    # print({k: len(sorted(set(key_values[k])))})
    for v in sorted(set(key_values[k])):
        print(c[v])
