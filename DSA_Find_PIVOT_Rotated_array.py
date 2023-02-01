arr=[7,8,9,10,11,12,13,1,2]
def Pivot(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+((end-start)//2)
        if arr[mid]<arr[mid-1]:
            return mid-1
        if arr[mid]>arr[mid+1]:
            return mid
        if arr[start]>arr[mid]:
            end=mid-1
        if arr[start]<arr[mid]:
            start=mid+1
    return -1
print(Pivot(arr))