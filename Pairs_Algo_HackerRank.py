# from itertools import permutations
# m=list(map(int,input().split()))
# x=list(map(int,input().split()))
# perm=list(permutations(x,2))
# z=[i for i in perm if (i[0]-i[1])==m[-1]]
# print(len(z))





def isodd(n):
    return (n & 1)==1
print(isodd(31))



def find_unique(arr):
    unique=0
    for i in arr:
        unique= unique^i
    return unique


print(find_unique([4,5,6,4,6,7,7]))