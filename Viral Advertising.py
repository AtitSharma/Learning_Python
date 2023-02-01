n=int(input())
Shared=[5]
Liked=[]
for i in range (n-1):
    Shared.append((Shared[i]//2)*3) 
liked=[i//2 for i in Shared ]
print(sum(liked))