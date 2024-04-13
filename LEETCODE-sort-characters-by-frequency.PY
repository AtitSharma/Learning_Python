s = "Aabbc"
new_dict = {}
for i in s :
    if new_dict.get(i):
        new_dict[i] +=1
    else:
        new_dict[i] = 1
print(new_dict)
new_sorted_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1],reverse=True)}
print(new_sorted_dict)

new_str = ''

for k,j in new_sorted_dict.items():
    new_str += k*j
print(new_str)




