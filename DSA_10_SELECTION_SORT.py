def Selection_Sort(arr):
    for i in range (len(arr)-1):
        start=0
        last=len(arr)-i-1
        Max_Num=Get_Max_Num(arr,start,last)
        Swap(arr,Max_Num,last)
    return arr
    

def Get_Max_Num(arr,start,last):
    max=start
    for i in range (start,last+1):
        if arr[max] < arr[i]:
            max=i

    return max


def Swap(arr,First,Second):
    temp=arr[First]
    arr[First]=arr[Second]
    arr[Second]=temp
    



print(Selection_Sort([9,8,3,4,2,1,0,100,110,19,0]))