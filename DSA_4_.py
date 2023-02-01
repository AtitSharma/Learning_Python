#Find maximum number fron array from binary search



arr=[4,5,6,7,8,4,3,2,1]
def Peek(arr):
    start=0
    end=len(arr)-1
    while start<end:
        mid=start+((end-start)//2)
        if arr[mid]>arr[mid+1]:
            end=mid
        else:
            start=mid+1

    return start


print(Peek(arr))
print(chr(ord('S')+1))