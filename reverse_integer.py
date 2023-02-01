import math


def Reverse(num):
    x=abs(num)
    digits=int(math.log10(x)+1)
    if num <0:
        m= helper(x,digits)
        return -1 * m

        
    else:
        return helper(x,digits)


def helper(num,digits):
    if num%10==num:
        return num
    rem=num%10
    return rem *int(pow(10,digits-1)) + helper(num//10,digits-1)
print(Reverse(120))