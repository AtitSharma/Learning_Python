a="5133336789123456@"
z=''
y=[]
for i in a:
    if (i in z) or (z==""):
        z+=i
    else:
        y.append(len(z))
        z=''
        z+=i
print(y)
x=[i for i in y if i>=4]
print(x)
if len(x)>=1:
    print("Invalid")
else:
    print("Valid")