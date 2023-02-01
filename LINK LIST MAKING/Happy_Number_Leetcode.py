def findsquare(num):
    ans=0
    while num>0:
        rem=num%10
        ans+=rem*rem
        num=num//10
    return ans
def ishappy(n):
    slow=n
    fast=n
    while True:
        slow=findsquare(slow)
        fast=findsquare(findsquare(fast))
        if slow==fast:
            break
    if slow==1:
        return True
    else:
        return False

# print(findsquare(19))
print(ishappy(2))
