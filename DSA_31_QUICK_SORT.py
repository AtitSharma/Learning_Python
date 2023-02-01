def Quick_Sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()
    greater=[]
    lower=[]
    for i in arr:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return Quick_Sort(lower)+[pivot]+Quick_Sort(greater)

arr=[1,100,2,3,35,43,5,46,547,56,6,324,5,2,5213,52,35,25,1]
print(Quick_Sort(arr))
