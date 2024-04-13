from collections import Counter

nums = [1,3,2,1,3,2,2]
counter = dict(Counter(nums))
# print(counter)
new_arr = []
sum = 0
for i,k in counter.items():
    sum+= k//2
    if k%2 !=0:
        new_arr.append(k)
    # print(i,k)


print([sum,len(new_arr)])





