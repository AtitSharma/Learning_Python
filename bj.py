a=int(input())
for num in range(2,a):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                break
        else: 
            print(num)
print("Hello")     
def fib(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,num):
        c=a+b
        a=b
        b=c
        print(c)
fib(int(input()))
