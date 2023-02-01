import numpy as np
a=list(map(int,input().split()))
arr=[]
for i in range (a[0]):
    listing=list(map(int,input().split()))
    arr.append(listing)
My_array=np.array(arr)
sum_=sum(My_array)
print(np.product(sum_))
