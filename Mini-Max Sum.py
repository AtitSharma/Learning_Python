from functools import reduce
My_List=list(map(int,input().split()))
sum1=[]
z=[]
for i in range (len(My_List)):
    a=My_List.copy()
    a.pop(i)
    sum1.append(sum(a))
z.append(reduce(min,sum1))
z.append(reduce(max,sum1))

for i in z:
    print(i,end=" ")