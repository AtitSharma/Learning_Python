
def Binary_SearchSqrt(a,b):
    s=0
    e=a
    root=0.0
    while s <= e:
        m=s+(e-s)/2
        if m*m == a:
            return m
            
        if m*m > a:
            e=m-1
        else:
            s=m+1
    increment=0.1
    for _ in range (0,b):
        while root * root <=a:
            root+=increment
        root-=increment
        increment /=10
    return root


print(Binary_SearchSqrt(a=15,b=4))


