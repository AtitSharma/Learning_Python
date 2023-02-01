a=int(input())
List=list(map(int,input().split()))
count=[]
for i in List:
    if i not in count:
        count.append(i)
Count1=[]
for i in count:
    Count1.append(List.count(i))
EvenNum=[]
OddNum=[]
for i in Count1:
    if i%2==0:
        EvenNum.append(i)
    else:
        OddNum.append(i)
count=0
for i in EvenNum:
    num=i//2
    count+=num
for i in OddNum:
    num1=i//2
    count+=num1

print(count)