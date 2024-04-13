nums = [-1,1,-6,4,5,-6,1,4,1]
# 3,3,2,2,1,1,1
nums.sort(reverse=True)
new_dict = {}
for i in nums :
    if new_dict.get(i):
        new_dict[i] +=1
    else:
        new_dict[i] = 1
print(new_dict)
new_dict1 = {k:v for k,v in sorted(new_dict.items(),key=lambda item: item[1],reverse=False)}
print(new_dict1)
new_arr=[]
for i,j in new_dict1.items():
    new_arr += [i]*j
print(new_arr)

# nums = [1,1,1,2,2,3,3]
