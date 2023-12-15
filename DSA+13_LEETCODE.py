# There must be all elemets in the array range(1,n)
# No dublicates
#No zeros

def Cyclic_Sort_Missing_Number(arr):
    i=0
    while (i <len(arr)):
        correct=arr[i]
        if (arr[i]<len(arr)) and (correct != arr[correct]):
            Swap(arr,i,correct)
        else:
            i+=1
    for i in range (0,len(arr)):
        if arr[i]!=i:
            return i  
    return len(arr)

def Swap(arr,start,end):
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
print(Cyclic_Sort_Missing_Number([4,5,6,3,1,2,0]))