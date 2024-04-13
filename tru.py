def findMin(arr):
        pivot=Pivot(arr)
        if pivot== -1:
            return arr[0]
        ans1=arr[pivot+1]
        
        return ans1

def Pivot(arr):
        start=0
        end=len(arr)-1
        while start <= end:
            mid=start+(end-start)//2
            if mid<end:
                if arr[mid] > arr[mid+1]:
                    return mid 
            if mid>start:
                if arr[mid] < arr[mid-1]:
                    return mid-1
            if arr[start]>=arr[mid]:
                end=mid-1
            if arr[start] < arr[mid]:
                start=mid+1
        return -1

print(findMin([2,3,4,5,5,1,1]))