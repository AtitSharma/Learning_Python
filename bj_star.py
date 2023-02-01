a=int(input())
count=0
count1=a-1
count2=0
for i in range (1,a+1):
    print((" "*(a-i))+("*"*(i+count)+" "*(a-i)))
    count+=1
for i in range (a,0,-1):
    print((" "*(a-i)+("*"*(i+count1))+" "*(a-i)))
    count1-=1
 