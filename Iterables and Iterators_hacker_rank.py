from itertools import combinations
EX=int(input())
My_List=list(map(str,input().split()))
num=int(input())
x=combinations("".join(My_List),num)
count_total,count_a=0,0
for i in x:
    count_total+=1
    if 'a' in i:
        count_a+=1
print(round(count_a/count_total,3))









