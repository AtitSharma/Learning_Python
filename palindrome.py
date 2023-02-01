import math
def Palindrome(num):
    if num<0:
        return "false"
    digits=int(math.log10(num)+1)
    if  helper(num,digits)==num:
        return 'true'
    else:
        return 'false'


def helper(num,digits):
    if num%10==num:
        return num
    rem=num%10
    return rem * int(pow(10,digits-1)) + helper(num//10,digits=digits-1)
print(Palindrome(-121))




