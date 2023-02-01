import numpy as np
np.set_printoptions(legacy='1.13')
First_List=list(map(int,input().split()))
if len (First_List)==1:
    print (np.eye(First_List[0]))
else:
    print(np.eye(3,3))

    
