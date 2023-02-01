inp=list(map(int,input().split()))
a=[]
b=[]
for i in range (inp[0]):
    a.append(input())
for i in range (inp[1]):
    b.append(input())
z=[]
Group_A=[]
for j in range (len(a)):
    for i in b:
        if i==a[j]:
            z.append(((j+1),i))
Group_B=[]

# print(z)
for i in z:
    if "a" in i:
        Group_A.append(i[0])
    elif "b" in i:
        Group_B.append(i[0])


# print(Group_A)
# print(Group_B)


# if "c" in b:
#     print(-1)
# for i in Group_A:
#     print(i,end=" ")
# print()
# for j in Group_B:
#     print(j,end=" ")


for i in a:
    if i in b:
        print(*Group_A)
        print(*Group_B)
    else:
        print(-1)
    break