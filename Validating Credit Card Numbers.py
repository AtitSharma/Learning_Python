import re
xyz=[]
for i in range (int(input())):
    a=input()
    pattern=r"^[4,5,6]"
    pattern2=r"^[4,5,6]\d{3}[-]\d{4}[-]\d{4}[-]\d{4}$"
    if re.match(pattern,a):
        if a.isalnum():
            if len(a)==16:
                for i in a:
                    if a.count(i)<=4:
                        xyz.append(a)
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")

    
print(xyz)

                        


                    



