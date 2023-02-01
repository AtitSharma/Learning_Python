def BinarySearch(list1,num):
    left_index=0
    Right_index=len(list1)-1
    mid_index=0

    while left_index <= Right_index:
        mid_index=(left_index+Right_index)//2
        mid_num=list1[mid_index]
        if mid_num==num:
            return mid_index
        if mid_num < num :
            left_index=mid_index+1       
        else:
            Right_index=mid_index-1
    return -1

list1=[1,2,3,4,7,9,10,32]
num=32

a=(BinarySearch(list1,num))
print(f'the number is found in {a}')