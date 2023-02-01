from itertools import combinations
a=int(input())
My_List=list(map(str,input().split()))
num=int(input())
My_List=(list(combinations(My_List,num)))
count=0
y=(My_List[0][0:num])
x=My_List[0][1]
for i in My_List:
    # print(i)
    if y in i:
        # print(i)
        count+=1
    elif x in i:
        # print(i)
        count+=1
# print(count)
print(count/len(My_List))
