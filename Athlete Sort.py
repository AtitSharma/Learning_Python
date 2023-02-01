n,m=map(int,input().split())
number=[list(map(int,input().split())) for i in range (n)]
ignored_num=int(input())
number.sort(key=lambda x: x[ignored_num])
for i in number:
    print(*i,end=' ')
    print()



