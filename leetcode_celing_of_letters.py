def Binary_Search(arr,num):
    start_index=0
    end_index=len(arr)-1
    mid_index=0
    while start_index <= end_index:
        mid_index=start_index+((end_index-start_index)//2)
        mid_num=arr[mid_index]
        if mid_num==num:
            pass
        if mid_num>num:
            end_index=mid_index-1
        else:
            start_index=mid_index+1
    return arr[start_index % len(arr)]
arr=eval(input())
target=input()
x=(Binary_Search(arr,target))
print('"' + x + '"')

