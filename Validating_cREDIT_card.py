#CORRECT HACKERRANK SOLUTION.
for i in range (int(input())):
    Credit=input()
    if Credit[0]=="4" or Credit[0]=="5" or Credit[0]== "6":
        if len(Credit)==16:
            if Credit.isdigit():
                z=""
                count1=[]
                Credit1=str(Credit)
                Credit1+="@"
                for i in Credit1:
                    if (i in z) or ( z==""):
                        z+=i
                    else:
                        count1.append(len(z))
                        z=""
                        z+=i
                x=[i for i in count1 if  i>=4]
                if len(x)>=1:
                    print("Invalid")
                else:
                    print("Valid")                   
                    
            else:
                print("Invalid")


        elif len(Credit)==19:
            if Credit[4]=="-" and Credit[9]=="-" and Credit[14]=="-":
                Credit1=Credit.replace("-","")
                if Credit1.isdigit():
                    z=""
                    count1=[]
                    Credit1=str(Credit1)
                    Credit1+="@"
                    for i in Credit1:
                        if (i in z) or ( z==""):
                            z+=i
                        else:
                            count1.append(len(z))
                            z=""
                            z+=i
                    x=[i for i in count1 if  i>=4]
                    if len(x)>=1:
                        print("Invalid")
                    else:
                        print("Valid")










                else:
                    print("Invalid")
                    
                        






            else:
                print("Invalid")

            





        else:
            print("Invalid")






    else:
        print("Invalid")


