num=9
import time


t1=time.time()
for i in range (2,num):
    prime=True
    if num%i==0:
        prime=False
        break
    else:
        prime=True
t2=time.time()  
print(prime, f"in {t2-t1} ")



t1=time.time()
for i in range (2,int(pow(num,0.5))):
    prime=True
    if num%i==0:
        prime=False
        break
    else:
        prime=True
t2=time.time()
print(prime, f"in {t2-t1} ")




t1=time.time()
for i in range (2,num//2):
    prime=True
    if num%i==0:
        prime=False
        break
    else:
        prime=True
t2=time.time()
print(prime, f"in {t2-t1} ")