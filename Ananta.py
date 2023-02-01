# a=int(input())
# x=[]
# for i in range (1,a+1):
#     x.append(str(i))
# zero=0
# count=3
# count1=6
# print(list(x[0]))
# print(list(x[1:3]))
# for i in range (2):
#     print(x[count:count1+zero])
#     count+=3
#     count1+=3
#     zero+=1
# count=0
# a=int(input())
# for i in range (1,a):
#     print((" "*(a-count))+"x"*i)
#     count+=1
    
    
def Summ(n):
    if n<=1:
        return n
    return n + Summ(n-1)

print(Summ(10))



def Multiplication (n,count=1):
    if count>10:
        return
    print(n*count)
    Multiplication(n,count+1)
Multiplication(7)
