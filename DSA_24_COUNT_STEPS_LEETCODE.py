def Count_Step(n):
    return helper(n,c=0)


def helper(n,c):
    if n==0:
        return c
    if n%2==0:
        return helper(n//2,c=c+1)
    return helper(n-1,c=c+1)
print(Count_Step(123))
