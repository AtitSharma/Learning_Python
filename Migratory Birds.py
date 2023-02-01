n=int(input())
Birds=list(map(int,input().split()))
Birds_Type=[]
for i in Birds:
    if i not in Birds_Type:
        Birds_Type.append(i)
print(Birds_Type)
Count=[]
for i in Birds_Type:
    Count.append(Birds.count(i))
print(Count)
NewLits=[]
Dict={}
for i in range (len(Count)):
    Dict[Birds_Type[i]]=Count[i]
    NewLits.append((Birds_Type[i],Count[i]))
print(Dict)
NewLits.sort(key=lambda x:x[0])
print(NewLits)
max=NewLits[0][1]
for i in NewLits:
    if i[1]>max:
        max=i