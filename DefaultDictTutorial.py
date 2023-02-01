from collections import defaultdict
dict=defaultdict(list)
List=[]
a=list(map(int,input().split()))
for i in range (a[0]):
    dict[input()].append(i+1)
for i in range (a[1]):
    List.append(input())
for i in List:
    if i in dict:
        print(" ".join(map(str,dict[i])))
    else:
        print(-1)