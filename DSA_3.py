# leetcode solution of next_greatest num



def next_Greatest_Num(arr,n):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+((end-start)//2)
        if n < arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return arr[start%len(arr)]






print(next_Greatest_Num(['c','i','j'],'j'))

        

