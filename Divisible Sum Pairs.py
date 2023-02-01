from  itertools import combinations
a=list(map(int,input().split()))
My_List=list(map(int,input().split()))
My_List=list(combinations(My_List,2))
# print(My_List)
z=[]
for i in My_List:
    if sum(i)%a[1]==False:
        z.append(1)

# print(z)

print(len(z))