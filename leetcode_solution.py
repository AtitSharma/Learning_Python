from itertools import combinations
arr=[2,7,11,15]
target=9
arr.sort()
z=[i for i in range(0,len(arr)) if arr[i]==target]
print(z)
m=[]
m.append(list(combinations(arr,2)))
print(m)
for i in m:
    for j in i:
        if sum(j)==target:
            l=j
            break
x=[arr.index(i) for i in l ]
print(x)