def Digits_Sum(n):
    if n==0:
        return 0
    else:
        return n%10 + Digits_Sum(n//10)

print(Digits_Sum(43))

