


def Sorted(arr,index):
    if index==len(arr)-1:
        return True
    return arr[index]<arr[index+1] and  Sorted(arr,index=index+1)
    
print(Sorted([1,2,3,4,5],0))