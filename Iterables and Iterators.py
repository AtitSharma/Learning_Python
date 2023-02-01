from itertools import combinations
num=int(input())
List=list(map(str,input().split()))
a=int(input())
My_list=list(combinations(List,a))
print(My_list)
Elements=List[0:a]
print(Elements)
count=0
for i in Elements:
    for j in My_list:
        if i in j:
            count+=1
print(count)