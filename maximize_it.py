import itertools
from functools import reduce
# a = [[1,2,3],[4,5,6],[7,8,9,10]]
# print( list(itertools.product(*a)))
Final_List=[]
new_list=[]
a=list(map(int,input().split()))
for i in range (a[0]):
    m_list=list(map(int,input().split()))
    m_list.remove(m_list[0])
    new_list.append(m_list)
# print(new_list)
very_new_list=(list(itertools.product(*new_list)))
# print(very_new_list)
# for i in very_new_list:
#         S=(reduce(lambda x,y:x+y,i))
#         # print(S)
#         # FINAL_ANSWER=(S)%a[1]
#         # Final_List.append(FINAL_ANSWER)
my_list=[]
for i in very_new_list:
    for x in i:
        eqn=x**2
        my_list.append(eqn)
# print(my_list)
my_list2=[]
count=a[0]
zer0=0
for i in my_list:
    sumi=sum(my_list[zer0:count])
    my_list2.append(sumi)
    count+=a[0]
    zer0+=a[0]

# print(my_list2)

Final_answer=(reduce(max,my_list2))
# print(Final_answer)
Required_Answer=Final_answer%a[1]
print(Required_Answer)

# print(Final_List)
# print(reduce(max,Final_List))

