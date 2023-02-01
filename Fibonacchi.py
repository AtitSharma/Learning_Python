def fib (n):
    a=0
    b=1
    if n<2:
        print("You cant get fibonacchi number")
    else:
        print(a)
        print(b)

        for i in range (2,n):
            c=a+b
            a=b
            b=c
            print(c)



n=int(input("How Many Fibonacchi numbers do you need\n"))

fib(n)