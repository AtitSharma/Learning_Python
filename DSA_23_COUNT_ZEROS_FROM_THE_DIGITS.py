def CountZeros(n):
    return helper (n,c=0)

def helper(n,c):
    if n==0:
        return c
    rem=n%10
    if rem==0:
        return helper (n//10,c=c+1)
    return helper(n//10,c)
print(CountZeros(302100))
