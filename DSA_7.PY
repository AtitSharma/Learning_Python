def Rotation_Count(arr):
    start=0
    end=len(arr)-1
    count=0
    if arr[start]>=arr[end]:
        while arr[start] >= arr[end]:
            mid=start+((end-start)//2)
            if arr[start]>arr[end]:
                start=start+1
                count+=1
        return count
    else:
        return 0
    


print(Rotation_Count([7,8,9,3,4,5]))


##   next   Method
#-----| this is faster

def Rotation_Count2(arr):
    start=0
    end=len(arr)-1 
    while start<end:
        mid=start+((end-start)//2)
        if arr[mid]>arr[mid+1]:
            return mid
        if arr[mid]<arr[mid-1]:
            return mid-1
        if arr[start]>arr[mid]:
            end=mid-1
        if arr[start]<arr[mid]:
            start=mid+1
    return -1


print(Rotation_Count2(([7,8,9,3,4,5]))+1)
