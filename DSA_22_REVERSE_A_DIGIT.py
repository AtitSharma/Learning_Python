import math
def rev(n):
    digits=int(math.log10(n)+1)
    return helper (n,digits)

def helper(n,digits):
    if n%10==n:
        return n
    remeder=n%10
    return  remeder * int(pow(10,digits-1)) +helper(n//10,digits-1)
print(rev(9988))





def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)

print(fibo(6))
