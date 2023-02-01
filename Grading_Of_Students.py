def Roundup(Marks):
    if Marks<38:
        print(Marks)
    else: 
        if (Marks+1)%5==False:
            print (Marks+1)
        elif (Marks+2)%5==False:
            print (Marks+2)
        else:
            print(Marks)

for i in range (int(input())):
    Marks=int(input())
    Roundup(Marks)