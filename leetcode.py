arr=[5,2,6,1]
new_list=[]
count=0
Max=arr[count]
newlist_=arr[count:]
print(new_list)
for i in range(len(newlist_)):
    if newlist_[i]<Max:
        new_list.append(newlist_[i])
    if i==newlist_:
        count+=1
    

    
  
print(new_list)

    
    