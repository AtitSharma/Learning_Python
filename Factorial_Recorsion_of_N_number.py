def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)
a=int(input())
print(Factorial(a))
