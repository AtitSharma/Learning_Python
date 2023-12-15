def Prod(n):
    if n < 1:
        return 1
    else:
        return n%10 * Prod(n//10)
print(Prod(52341))