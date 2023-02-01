def Back(r,c):
    if r==1 or c==1:
        return 1
    right=Back(r-1,c)
    left=Back(r,c-1)
    return right+left


print(Back(3,9))