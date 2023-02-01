def Rotated_Array(arr,target,s,e):
    if s>e:
        return -1
    m=s+((e-s)//2)
    if arr[m]==target:
        return m
    if arr[s]<=arr[m]:
        if target <=arr[m] and target  >= arr[s]:
            return Rotated_Array(arr,target,s,e=m-1)
        else:
            return Rotated_Array(arr,target,s=m+1,e=e)
    if target >= arr[m] and target <= arr[e]:
        return Rotated_Array(arr,target,s=m+1,e=e)
    else:
        return Rotated_Array(arr,target,s=s,e=m-1)
arr=[5,6,7,8,9,1,2,3]
print(Rotated_Array([5,6,7,8,9,1,2,3],3,s=0,e=len(arr)-1))