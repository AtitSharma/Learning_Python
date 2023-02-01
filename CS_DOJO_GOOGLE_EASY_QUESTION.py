#number must be 0-9 in the list


def find(arr):
    s=0
    e=len(arr)-1
    x=(len(arr)+1)*[0]
    x[0]=1
    while (s<=e):
        if arr[e]>8:
            arr[e]=0
            e-=1
        elif arr[e]<=8:
            arr[e]+=1
            return arr
    return x
print(find([9,9,9,9]))