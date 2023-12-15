import time
l=[1,0,1,0,0,0,1,0,1,0,1]*10000000

t1 = time.time()
zeros = l.count(0)
ones = l.count(1)
r = [0]*zeros + [1]*ones
t2 = time.time()
print(f"Time Taken by Count method is: {t2-t1}")
t1 = time.time()
zeros=[]
ones=[]

for i in l:
    if i==0:
        zeros.append(i)
    if i==1:
        ones.append(i)
r = zeros+ones
t2 = time.time()
print(f"Time Taken by Single loop method is: {t2-t1}")
