import numpy as np
a=int(input())
arr=[]
for i in range (a):
    a=list(map(float,input().split()))
    arr.append(np.array(a))
b=float(np.linalg.det([arr]))
print(round(b,2))
    
