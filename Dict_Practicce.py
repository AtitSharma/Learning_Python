Price=0
dict={}
for i in range (int(input())):
    lis=list(map(str,input().split()))
    print(lis)
    Fruits=lis[0:-1]
    Fruits=" ".join(Fruits)
    Price=int(lis[-1])
    dict[Fruits]=Price
    dict[Fruits]+=dict[Fruits]
print(dict)
