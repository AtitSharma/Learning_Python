from itertools import permutations
a=int(input())
My_List=list(map(int,input().split()))
num=My_List[0]
perm=permutations(My_List,2)
listed_perm=(list(perm))
setted_perm=(set(listed_perm))
List=[]
for i in setted_perm:
    if abs(i[0]-i[1])<=1:
        List.append(i[0])

print(List)