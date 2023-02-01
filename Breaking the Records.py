a=int(input())
score=list(map(int,input().split()))
max=score[0]
min=score[0]
best=0
worst=0
for i in score:
    if i>max:
        best+=1
        max=i
for i in score:
    if i<min:
        worst+=1
        min=i
print(best,worst)