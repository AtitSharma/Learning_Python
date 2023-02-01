import operator
from collections import deque
from itertools import accumulate
# x=[1,2,3,4]
# a=deque(x)
# print(a)
# a.appendleft(0)
# a.appendleft(100)
# a.extend([9,10])
# a.pop()
# print(a)
# a.rotate(3)
# print(a)
# a.rotate(-3)
# print(a)


# z=[1,2,3,4]
# z=accumulate(z)
# print(list(z))
# z=[1,2,3,4]
# z=accumulate(z,func=operator.mul)
# print(list(z))

from itertools import groupby

def smaller_Than(x):
    return x<4



x=[1,2,3,4,5]
group=groupby(x,key=smaller_Than)
group=groupby(x,key=lambda m: m<3)
for key , value in group:
    print(key,list(value))