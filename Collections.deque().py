from collections import deque
d = deque()
z=[]
for i in range(int(input())):
    a=list(map(str,input().split()))
    if a[0]=="append":
        d.append(a[1])
    if a[0]=="appendleft":
        d.appendleft(a[1])
    if a[0]=="pop":
        d.pop()
    if a[0]=="popleft":
        d.popleft()
# print(d)
for i in d:
    print(i,end=" ")