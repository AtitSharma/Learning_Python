from itertools import combinations
ex=int(input())
My_List=list(map(str,input().split()))
First=[]
num=int(input())
for i in range (num):
    for j in My_List:
        First.append(j)
print(First)
My_List=(list(combinations(My_List,num)))
# print(My_List)
count=0
# for i in My_List:
#     if First in i:
#         count+=1
#     if Second in i:
#         count+=1
#     if (First and Second) in i :
#         count-=1
# print(count/len(My_List))