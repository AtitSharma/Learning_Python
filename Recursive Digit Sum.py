def Digit(n, k):
    summ = str(eval('+'.join(str(n)*k)))
    if len(summ) == 1:
        return summ
    else:
        return Digit(summ, 1)
a=list(map(int,input().split()))
print(Digit(a[0],a[1]))




