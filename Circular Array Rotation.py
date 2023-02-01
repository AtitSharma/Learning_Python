from collections import deque
a=list(map(int,input().split()))
My_List=list(map(int,input().split()))
x=deque(My_List)
x.rotate(a[1])
for i in range (a[-1]):
    print(x[int(input())])