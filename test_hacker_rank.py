a="Fizz"
b="Buzz"
My_List=[]
inp=int(input())
for i in range (1,inp+1):
    My_List.append((i))
My_Newlist=[]
for i in range (1,inp+1):
    if (i % 3 or i%5)==False:
        print("FizzBuzz")
    elif i%3==False:
            print("Fizz")
    elif i%5==False:
            print("Buzz")
    else:
        print(i)