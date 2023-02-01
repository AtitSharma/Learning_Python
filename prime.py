a=int(input())
for i in range(2,a):
    if a>1:
        for k in range (2,i):
            if i%k==0:
                break
        else:
            print(i)