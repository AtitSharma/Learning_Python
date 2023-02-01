n=-1
k=int(input())
for _ in range (k):
    s=input()
    while len(s) !=n:
        n=len(s)
        s=s.replace('[]','')
        s=s.replace('()','')
        s=s.replace('{}', '')
    if len(s)==0:
        print('YES')
    else:
        print("NO")