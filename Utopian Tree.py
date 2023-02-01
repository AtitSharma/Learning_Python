from functools import reduce
n=int(input())
z=[1]
m=1
num=[int(input()) for i in range(n)]
loop1=max(num)
for i in range (1,loop1+1):
    lat=(m*2)
    z.append(lat)
    v=(lat+1)
    z.append(v)
    m=v

for i in num:
    print(z[i])