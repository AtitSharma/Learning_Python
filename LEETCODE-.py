



def helper(nums):
    Sum = 0
    Total_Sum =0
    for i in nums :
        Sum += i
        if Sum > Total_Sum:
            Total_Sum = Sum
        if Sum < 0 :
            Sum = 0
    return Total_Sum
    
    
print(helper([-2,1,-3,4,-1,2,1,-5,4]))