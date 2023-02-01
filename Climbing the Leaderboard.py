a=int(input())
list1=list(map(int,input().split()))
b=int(input())
list2=list(map(int,input().split()))
New_list=[]
for i in list1:
    if i not in New_list:
        New_list.append(i)
for i in list2:
    New_list.append(i)
    New_list.sort()
    New_list.reverse()
    print(New_list.index(i)+1)
    New_list.remove(i)