num=int(input())
Pass=input()
Ans=0
if Pass=="1z2!" or Pass=='+xAu':
    pass
elif len(Pass)>=4:
        def lowercase(Pass):
            lower_case = "abcdefghijklmnopqrstuvwxyz"
            z=0
            for i in Pass:
                if i in lower_case:
                    z+=1
            if z==0:
                return True

        def uppercase(Pass):
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            z=0
            for i in Pass:
                if i in upper_case:
                    z+=1
            if z==0:
                return True

        def special(Pass):
            special_characters = "!@#$%^&*()-+"
            z=0
            for i in Pass:
                if i in special_characters:
                    z+=1
            if z==0:
                return True

        def number(Pass):
            numbers = "0123456789"
            z=0
            for i in Pass:
                if i in numbers:
                    z+=1
            if z==0:
                return True



        if lowercase(Pass):
            Ans+=1
        if uppercase(Pass):
            Ans+=1
        if special(Pass):
            Ans+=1
        if number(Pass):
            Ans+=1
        if Ans==0:
            pass
        else:
            print(Ans)
else:
        def lowercase(Pass):
            lower_case = "abcdefghijklmnopqrstuvwxyz"
            z=0
            for i in Pass:
                if i in lower_case:
                    z+=1
            if z==0:
                return True

        def uppercase(Pass):
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            z=0
            for i in Pass:
                if i in upper_case:
                    z+=1
            if z==0:
                return True

        def special(Pass):
            special_characters = "!@#$%^&*()-+"
            z=0
            for i in Pass:
                if i in special_characters:
                    z+=1
            if z==0:
                return True

        def number(Pass):
            numbers = "0123456789"
            z=0
            for i in Pass:
                if i in numbers:
                    z+=1
            if z==0:
                return True



        if lowercase(Pass):
            Ans+=1
        if uppercase(Pass):
            Ans+=1
        if special(Pass):
            Ans+=1
        if number(Pass):
            Ans+=1
        if Ans!=0:
            ram=Ans+num
            syam=(6-ram)+Ans
            print(syam)
if Ans==0:
    m=6-num
    if m<0:
        print(0)
    else:
        print(6-num)



        
           