from functools import reduce
int(input())
My_List=list(map(int,input().split()))
Higest_App=[]
for i in My_List:
    Higest_App.append((My_List.count(i),i))
Higest_App=reduce(max,Higest_App)
ham=(Higest_App[-1])
Final_List=[]
for i in My_List:
    if i ==ham:
        Final_List.append(i)
print(len (My_List)-len(Final_List))