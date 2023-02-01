#!/usr/bin/env python3
from itertools import combinations
a=list(map(str,input().split()))
z=[]
for i in a[0]:
    z.append(i)
z.sort()
for i in z:
    print(i)
xyz=[]
for i in range(2,(int(a[1])+1)):
    a= (list(combinations(z,i)))
    xyz.append(a)
for i in xyz:
    for j in i:
        print("".join(j))