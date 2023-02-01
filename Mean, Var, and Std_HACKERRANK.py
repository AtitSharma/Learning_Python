import numpy as np
np.set_printoptions(legacy='1.13')
a=list(map(int,input().split()))
My_arr=[]
for i in range (a[0]):
    arr=list(map(int,input().split()))
    My_arr.append(arr)
array1=np.array(My_arr)
print(np.mean(array1,axis=1))
print(np.var(array1,axis=0))
print(np.std(array1,axis=None))