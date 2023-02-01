
arr=[7,8,9,0,0]
def Answer(arr):
    if len(arr)<=1:
        return [0]
    new_arr=[]
    s=0
    e=len(arr)-1
    a=0
    while s<=e:
        if arr[s]>arr[e]:
            a+=1
            e-=1
        else:
            e-=1
        if s==e:
            s+=1
            e=len(arr)-1
            new_arr.append(a)
            a=0
        if e==s:
            new_arr.append(0)
    return new_arr





print(Answer(arr))