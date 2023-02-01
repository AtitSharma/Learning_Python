a=[]
b=[]
my_NUm=[]
for i in range (int(input())):
    a.append(input())
for i in range (int(input())):
    b.append(input())
for i in b:
    my_count=a.count(i)
    my_NUm.append(my_count)
# print(my_NUm)
for i in my_NUm:
    print(i)