def LinearSearch(arr,target,index):
    if index==len(arr)-1:
        return -1
    elif arr[index]==target:
        return index
    else:
        return LinearSearch(arr,target,index=index+1)
print(LinearSearch([5,4,1,3,5,1],1,0))
