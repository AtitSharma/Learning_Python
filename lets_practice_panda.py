import numpy as np
np.set_printoptions(legacy='1.13')
a=list(map(float,input().split()))
my_array=np.array(a)
print(np.floor(my_array))
print (np.ceil(my_array))
print (np.rint(my_array))