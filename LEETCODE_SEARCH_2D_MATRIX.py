
# https://leetcode.com/problems/search-a-2d-matrix/description/


def is_available(arr,num) :
    start = 0
    end = len(arr)-1
    while start <= end :
        mid = (start + end) //2 
        if num in arr[mid]:
            return True
        if num < arr[mid] [0]:
            end = mid-1 
        else :
            start = mid + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 60
print(is_available(matrix,target))