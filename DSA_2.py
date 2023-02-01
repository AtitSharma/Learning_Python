#Binary Search Program
arr=[5]
def Binary_Search(arr,num):
    start_index=0
    end_index=len(arr)-1
    mid_index=0
    while start_index <= end_index:
        mid_index=start_index+((end_index-start_index)//2)
        mid_num=arr[mid_index]
        if mid_num==num:
            return mid_index
        if mid_num>num:
            end_index=mid_index-1
        else:
            start_index=mid_index+1
    return -1 
x=(Binary_Search(arr,5))
print(x)




arr1=[90,80,15,11,5,1,0]
def Binary_Search2(arr1,num):
    start_index=0
    end_index=len(arr1)-1
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

     
x=(Binary_Search2(arr1,0))
print(x)
