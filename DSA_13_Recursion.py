# def message():
#     print("Hello World1")
#     message1()

# def message1():
#     print("Hello World2")
#     message2()

# def message2():
#     print("Hello World3")
#     message3()

# def message3():
#     print("Hello World4")
#     message4()

# def message4():
#     print("Hello World5")
# message()





# def printf(n):
#     if n==5:
#         print(n)
#         return
#     print(n)
#     printf(n+1)
# printf(1)



def Fibo_NuM(n):
    if n<2:
        return n
    
    return Fibo_NuM(n-2)+Fibo_NuM(n-1)

print(Fibo_NuM(5))




def fibonacchi(num):
    if num < 2:
        return num
    else:
        return fibonacchi(num-2 )+ fibonacchi(num-1)
n=int(input())
for i in range (n):
    print(fibonacchi(i))