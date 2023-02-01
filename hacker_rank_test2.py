import numpy as np
Altimate_list=[]
inp=list(map(int,input().split()))
A_list=[]
B_List=[]
for i in range (inp[0]):
    A=list(map(int,input().split()))
    A_list.append(A)
    B=list(map(int,input().split()))
    B_List.append(B)

    # print(A+B)
    # print(A-B)
    # print(A*B)
    # print(A//B)
    # print(A%B)
    # print(A**B)
My_New_List=np.array(A_list)
My_New_List2=np.array(B_List)
for i in range (inp[0]):
    addition=My_New_List[0]+My_New_List[1]
    Altimate_list.append(addition)
    subtraction=My_New_List[0]-My_New_List[1]
    Altimate_list.append(subtraction)
    mul=My_New_List[0]*My_New_List[1]
    Altimate_list.append(mul)
    div=My_New_List[0]//My_New_List[1]
    Altimate_list.append(div)
    per=My_New_List[0]%My_New_List[1]
    Altimate_list.append(per)
    sqr=My_New_List[0]**My_New_List[1]
    Altimate_list.append(sqr)

for i in Altimate_list:
    print(np.array(i,2))
