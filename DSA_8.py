def Split_Arr(arr):
    m=2
    start=max(arr)
    end=sum(arr)
    mid=start+((end-start)//2)
    while start<end:
        num=0
        pieces=1
        mid=start+((end-start)//2)
        for i in arr:
            if  num+i >mid:
                num=i
                pieces+=1
            else:
                num+=i
        if pieces>m:
            start=mid+1
        else:
            end=mid
    return start

print(Split_Arr([7,2,5,8,10]))

