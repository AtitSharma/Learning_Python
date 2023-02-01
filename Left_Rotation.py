b=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range (b[1]):
    a.append(a[0])
    a.pop(0)
# print(a)
for i in a:
    print(i,end=" ")