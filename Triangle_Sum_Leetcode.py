def sumtriangle(nums):
    if len(nums)==1:
        return nums[0]
    newlist=[]
    if (len(newlist)==1) and (len(nums)==1):
        return newlist[0]
    for i in range(len(nums)-1):
        ans=(nums[i]+nums[i+1])%10
        newlist.append(ans)
    return sumtriangle(newlist)
print(sumtriangle([1,2,3,4,5]))