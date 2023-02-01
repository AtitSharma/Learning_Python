n=int(input())
z=[]
for i in range (1,n+1):
    if (i%3 or i%5 )==False:
        z.append("FizzBuzz")
    elif i%5==False:
        z.append('Buzz')
    elif i%3==False:
        z.append('Fizz')
    # elif i%5==False:
    #     z.append("Buzz")
    else:
        z.append(str(i))
print(z)

    

