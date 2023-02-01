def Bubble_sort(arr,r,c):
    if r==c:
        return arr
    if c<r:
        if arr[c]>arr[c+1]:
            temp=arr[c]
            arr[c]=arr[c+1]
            arr[c+1]=temp
        return Bubble_sort(arr,r,c=c+1)
    else:
        return Bubble_sort(arr,r-1,c=c)

arr=[100,2,3,4,5,9,8,10,100,199,111,122]
print(Bubble_sort(arr,len(arr)-1,0))