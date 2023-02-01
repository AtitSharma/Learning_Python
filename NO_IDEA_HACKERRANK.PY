a=list(map(int,input().split()))
my_list=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))

HAPPPY_NESS=0
for i in A:
    if i in my_list:
        HAPPPY_NESS+=1
for i in B:
    if i in my_list:
        HAPPPY_NESS-=1
print(HAPPPY_NESS)

