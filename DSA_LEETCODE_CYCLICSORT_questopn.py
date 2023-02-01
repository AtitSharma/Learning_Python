def Cyclic_Sort_Doublicate_Number(arr):
    i=0
    while (i <len(arr)):
        correct=arr[i]-1
        if arr[i] != arr[correct]:
            Swap(arr,i,correct)
        else:
            i+=1
    z=[]
    for k in range (0,len(arr)):
        if arr[k]!=k+1:
            z.append(k+1)
    return z

def Swap(arr,start,end):
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp



print(Cyclic_Sort_Doublicate_Number([4,3,2,7,8,2,3,1]))