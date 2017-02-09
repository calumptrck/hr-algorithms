#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
distance = abs(x1-x2)
velocity = abs(v1-v2)

if (v1==v2):
    print('NO')
else:
    meet = float((x2-x1) / (v1-v2))
    if (meet<1 or meet%1!=0):
      print('NO')
    else:
     print('YES')