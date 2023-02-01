xyz=[]
for i in range (int(input())):
    a=input()
    u=0

    for i in a:
        if i.isupper():
            u+=1
    if (u>1):
        num=0
        for j in a:
            if j.isnumeric():
                num+=1
        if num>2:
            if a.isalnum():
                if len(a)==10:
                    similar=0
                    for x in a:
                        for y in a:
                            if (x==y):
                                similar+=1
                    if similar==10:
                        print("Valid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")



    


                


    
    
