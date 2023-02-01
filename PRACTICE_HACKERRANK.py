a=int(input())
My_Num=[]
Sec_Num=[]
for i in range (3):
    Num=list(map(str,input().split()))
    My_Num.append(Num)
for i in My_Num:
    for j in i:
        print(type(j))
        if len(j)<12:
            Small_Num="+91"+j
            Sec_Num.append(Small_Num)
        else:
            Sec_Num.append(j)
print(Sec_Num)
