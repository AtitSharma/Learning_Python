import re
from itertools import combinations
vowels=["a","e","i","o","u","A","E","I","O","U"]
New_List=[]
my_list=[]
for i in range (1,len(vowels)):
    comb=list(combinations(vowels,i))
    New_List.append(comb)
# print(New_List)
for i in New_List:
    for j in i:
        xy="".join(j)
        my_list.append(xy)
    print()

print(my_list)
for i in my_list:
    if i in "rabcdeefgyYhFjkIoomnpOeorteeeeet":
        print(i)
