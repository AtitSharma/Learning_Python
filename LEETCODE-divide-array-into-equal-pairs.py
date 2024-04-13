nums = [3,2,3,2,2,2]
arr = []
for i in nums :
    if nums.count(i) % 2 == 0:
        arr.append(True)
    else :
        arr.append(False)
print(all(arr))
        