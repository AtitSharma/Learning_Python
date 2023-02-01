from collections import  namedtuple
n=int(input())
data=namedtuple('data',input().split())
s=0
for i in range (n):
    marks=(data(*input().split()).MARKS)
    s+=int(marks)
print(s/n)
