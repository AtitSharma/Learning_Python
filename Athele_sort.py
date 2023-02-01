Newlist=[]
a=list(map(int,input().split()))
for i in range (a[0]):
    List=tuple(map(int,input().split()))
    Newlist.append(List)

Ignored_Number=int(input())
Newlist.sort(key=lambda x:x[Ignored_Number], reverse=True)
# print(Newlist)
My_New_List=(Newlist[-1::-1])
# print(My_New_List)
for i in My_New_List:
    for j in i:
        print(j,end=" " )
    print()