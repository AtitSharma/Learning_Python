def valid(num):

    if num[0]==4 or 5 or 6:
        if len(num)==19:
            if (num[4] or num[9] or num[14])=="-":
                y=[]
                for i in num:
                    y.append(i)
                for i in y:
                    if i=="-":
                        y.remove(i)        
                num="".join(y)
                try:
                    num=int(num)
                except:
                    return ("Invalid")
                
                z=[]
                for i in (str(num)):
                    z.append(i)
                for i in z:
                    if z.count(i)>=4:
                        return("Invalid")
                    else:
                        return("Valid")
            else:
                return("Invalid")
        if len((num))==16:
            try:
                num=int(num)
            except:
                return "Invalid"
            
            z=[]
            for i in (str(num)):
                    z.append(i)
            for i in z:
                if z.count(i)>=4:
                    return("Invalid")
                else:
                    return("Valid")
        else:
            return("Invalid")
    else:
        return("Invalid")




if __name__ == '__main__':
    a=int(input())
    for i in range (a):
        z=str(input())
        print(valid(z))
    