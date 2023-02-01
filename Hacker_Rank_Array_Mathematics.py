import numpy as np
a=list(map(int,input().split()))
xyz=[]
Decent_List=[]
for i in range (a[0]*a[0]):
    A=list(map(int,input().split()))
    xyz.append(A)

for i in xyz:
    if i not in Decent_List:
        Decent_List.append(i)
print(Decent_List)
for i in range (a[0]):
    print(Decent_List)
