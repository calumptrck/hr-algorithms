#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
nums=[a,b,c,d,e]
sums=[]
for x in range(0,5):
    sums.append(sum(nums)-nums[x])
print('%s %s'%(min(sums),max(sums)))