arr=[2,5,6,0,0,1,2]
def Find_Answer(arr,target):
    ram=Peek(arr)
    Left=Binary_Search(arr,s=0,e=ram,target=target)
    Right=N_Binary_Search(arr,s=ram+1,e=len(arr)-1,target=target)
    if Left==False and Right==False:
        return "false"
    else:
        return "true"


def Binary_Search(arr,s,e,target):
    while s<=e:
        m=s+((e-s)//2)
        if arr[m]==target:
            return True
        elif target > arr[m]:
            s=m+1
        else:
            e=m-1
    return False

def N_Binary_Search(arr,s,e,target):
    while s<=e:
        m=s+((e-s)//2)
        if arr[m]==target:
            return True
        elif target < arr[m]:
            s=m+1
        else:
            e=m-1
    return False

def Peek(arr):
    start=0
    end=len(arr)-1
    while start<end:
        mid=start+((end-start)//2)
        if arr[mid]>arr[mid+1]:
            end=mid
        else:
            start=mid+1

    return start
print(Find_Answer(arr,0))