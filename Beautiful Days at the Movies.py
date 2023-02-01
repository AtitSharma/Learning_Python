My_list=list(map(int,input().split()))
z=[i for i in range (My_list[0],My_list[1]+1)]
count=0
for i in z:
    v=str(i)
    if (abs(int(v)-int(v[::-1])))%My_list[-1]==0:
        count+=1
print(count)