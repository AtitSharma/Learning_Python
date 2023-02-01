from itertools import combinations
EX=int(input())
My_List=list(map(str,input().split()))
First=My_List[0]
try:
    Second=My_List[1]
    num=int(input())
    My_List=(list(combinations(My_List,num)))
    # print(My_List)
    count=0
    for i in My_List:
        if First in i:
            count+=1
        if Second in i:
            count+=1
        if (First and Second) in i :
            count-=1
    print(count/len(My_List))
except:
    num=int(input())
    My_List=(list(combinations(My_List,num)))
    count=0
    for i in My_List:
        if First in i:
            count+=1
    print(count/len(My_List))









