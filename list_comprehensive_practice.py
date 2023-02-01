# a=[1,2,3,4,5,1]
# x=[i for i in a if a.count(i)<2]
# print(x)
from itertools import  product
x=int(input())
y=int(input())
z=int(input())
n=int(input())
fst=[i for i in range (x+1)]
sec=[i for i in range (y+1)]
thi=[i for i in range (z+1)]
final=fst+sec+thi
lamo=list(product(fst,sec,thi))
newlist=[i for i in lamo if sum(i)!=n]
newlist=set(newlist)
newlist=list(newlist)
newlist.sort()
newlist=[list(i) for i in newlist]
print(newlist)