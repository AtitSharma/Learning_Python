##Program to get prime or not
num=int(input())
c=2
if num<=3:
    print("Prime")
c=2
while c <= int(pow(num,1/2)):
    if num%c==0:
        print("NOT Prime")
        break
    c=c+1
    if num%c!=0:
        print("Prime")
        break




def findPrime(num):
    if num<=3:
        return True
    c=2
    while c <= int(pow(num,1/2)):
        if num%c==0:
            return False
        c=c+1
        if num%c!=0:
            return True
num=20
for i in range (num):
    print(findPrime(i),i)
    

x=20
for i in range (2,x):
    if x>1:
        for k in range (2,i):
            if i%k==0:
                break
        else:
            print(i)
