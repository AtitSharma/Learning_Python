import numpy as np
my_arr=[]
a=int(input())
if a==2:
    for i in range (a):
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        my_arr.append(A)
        my_arr.append(B)
    arr=np.array([[my_arr[0],my_arr[1]],[my_arr[2],my_arr[3]]])

    A=arr[0,0],arr[0,1]
    B=arr[1,0],arr[1,1]
    print(np.dot(A,B))
else:
    for i in range (2):
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        C=list(map(int,input().split()))
        my_arr.append(A)
        my_arr.append(B)
        my_arr.append(C)
    A=np.array([my_arr[0],my_arr[1],my_arr[2]])
    B=np.array([my_arr[3],my_arr[4],my_arr[5]])
    print(np.dot(A,B))


