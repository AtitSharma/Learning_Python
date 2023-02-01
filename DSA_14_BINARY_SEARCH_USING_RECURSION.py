def BinarySearch(arr,n,s,e):
    if s>e:
        return -1
    m=s+(e-s//2)
    if arr[m]==n:
        return m
    elif n > arr[m]:
        return BinarySearch(arr,n,s=m+1,e=len(arr)-1)
    elif n < arr[m]:
        return BinarySearch(arr,n,s,e=m-1)
arr=[1,2,3,4,5,7,8,9,100]
print(BinarySearch(arr,n=1,s=0,e=len(arr)-1))
