a=list(map(int,input().split()))
b=list(map(int,input().split()))
Location_Of_Apple=b[0]
Location_of_Orange=b[1]
c=list(map(int,input().split()))
Distance_Of_Apple=(list(map(int,input().split())))
Distance_of_Orange=(list(map(int,input().split())))
Ans=[]
Ans2=[]
for i in Distance_Of_Apple:
    Ans.append(i+Location_Of_Apple)
for j in Distance_of_Orange:
    Ans2.append(j+Location_of_Orange)
count=0
count1=0
for i in range (a[0],a[1]+1):
        if i in Ans:
            count+=1
        if i in Ans2:
            count1+=1
print(count)
print(count1)




