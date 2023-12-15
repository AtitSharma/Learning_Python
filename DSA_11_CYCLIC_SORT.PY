# There must be all emeents in the array range(1,n)
# No dublicates
#No zeros

def Cyclic_Sort(arr):
    i=0
    while (i <len(arr)):
        correct=arr[i] # Do -1 if arr starts from 1
        if arr[i] != arr[correct]:
            Swap(arr,i,correct)
        else:
            i+=1
    return arr

def Swap(arr,start,end):
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp

print(Cyclic_Sort([0,3,2,1,7,6,5,9,10,11,12,4,8]))