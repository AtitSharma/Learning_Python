def LiS(arr,target,index,NewList=[]):
    if arr[index]==target:
        NewList.append(index)
    if index==len(arr)-1:
        return NewList
    return LiS(arr,target,index=index+1)

print(LiS([4,2,3,4,4,4,5],5,0))
