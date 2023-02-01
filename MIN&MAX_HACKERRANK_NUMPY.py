import numpy as np
a=list(map(int,input().split()))
My_=[]
for i in range (a[0]):
    arr=list(map(int,input().split()))
    My_.append(arr)
My_array=np.array(My_)
minimum=np.min(My_array,axis=1)
print(np.max(minimum))