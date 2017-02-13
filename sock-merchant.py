#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

pairs=0
used = set([])
for x in c:
  if c.count(x)>=2 and x not in used:
    used.add(x)
    pairs+=c.count(x)//2
print(pairs)
