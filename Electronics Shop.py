
import itertools
from functools import reduce
happy=list(map(int,input().split()))
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
x=(list(itertools.product(list1,list2)))
Max=[sum(i) for i in x]
for i in Max:
    if i>happy[0]:
        Max.remove(i)
try:
    print(reduce(max,Max))
except:
    print(-1)
    




