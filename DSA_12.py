def Cyclic_Sort_Missing_Number(arr):
    i=0
    while (i < len(arr)):
        correct=arr[i]-1
        if (arr[i]>0 and arr[i]<=len(arr) and arr[i] != arr[correct]) :
            Swap(arr,i,correct)
        else:
            i+=1

    for k in range (0,len(arr)):
        if arr[k]!=k+1:
            return k+1 
    return len(arr)+1

def Swap(arr,start,end):
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
print(Cyclic_Sort_Missing_Number([1,3,-1,4]))