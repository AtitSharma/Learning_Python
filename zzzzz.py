a=[7,2,5,10,8]
t=21
c=0
cc=1
for i in a:
    c+=i
    if c>t:
        cc+=1
        c=0

print(cc)
c=0
cc=1
t=21

for i in a:
    if (c+i>t):
        c=i
        cc+=1
    else:
        c+=i
print(cc)



def Fibonaacho(n):
    if n<=1:
        return 1
    else:
        return n+Fibonaacho(n-1)

print(Fibonaacho(100))


