import json
from collections import defaultdict

counts = {}
for l in open("main.json"):
    o = json.loads(l)
    if o is None:
        continue
    for k, v in o.items():
        if k not in counts:
            counts[k] = defaultdict(int)
        counts[k][v] += 1

for k in counts:
    for v in counts[k]:
        if counts[k][v] < 3:
            continue
        print(k, v)
#        print(repr((k, v)))
#        print(repr((k, v)))
