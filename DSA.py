#GOOGLE AND FACEBOOK INTERVIEW QUESTION



arr=[1,2,2,2,2,3,3,3,3,3,4,5]
def Search(arr,num,Khojam):
    s=0
    e=len(arr)-1
    ans=-1
    while s<=e:
        mid=s+((e-s)//2)
        if num < arr[mid]:
            e=mid-1
        elif num > arr[mid]:
            s=mid+1
        else:
            ans=mid
            if (Khojam==True):
                e=mid-1
            else:
                s=mid+1
    return ans


def main(arr,num):
    first_occurance=Search(arr,num,Khojam=True)
    print(first_occurance)
    last_occurance=Search(arr,num,Khojam=False)
    print(last_occurance)
main(arr,2)