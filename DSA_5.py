
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

def Order(arr1,num,start_index,end_index):
    mid_index=0
    while start_index<=end_index:
        mid_index=start_index+((end_index-start_index)//2)
        mid_num=arr1[mid_index]
        if mid_num==num:
            return mid_index
        if mid_num<num:
            end_index=mid_index-1
        else:
            start_index=mid_index+1
    return -1 
def Search(arr,target):
    peek=Peek(arr)
    first_=Order(arr,target,start_index=0,end_index=peek)
    print(first_)
    if first_!=-1:
        return first_
    else:
        return Order(arr,target,start_index=peek+1,end_index=len(arr)-1)
    
print(Search([7,8,9,10,3,4,5],3))

