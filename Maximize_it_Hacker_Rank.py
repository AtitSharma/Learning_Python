import itertools
from functools import reduce
a=list(map(int,input().split()))
First_list=[]
for i in range (a[0]):
    First=list(map(int,input().split()))
    First.remove(First[0])
    First_list.append(First)
very_new_list=(list(itertools.product(*First_list)))
# print(very_new_list)
# new_very_new_list=[]
# for i in very_new_list:
#     for j in i:
#         eqn=j**2
#         new_very_new_list.append(eqn)
# print(new_very_new_list)
# my_list=[]
# count=0
# count1=a[0]
# for i in new_very_new_list:
#     xyz=new_very_new_list[count:count1]
#     my_list.append(xyz)
#     count+=a[0]
#     count1+=a[0]
# print(my_list)
output=list(map(lambda array : sum(map(lambda x : x**2, array)),very_new_list))
# print(output)

listing=[]
for i in output:
    final=i%a[1]
    listing.append(final)

print(reduce(max,listing))