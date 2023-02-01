a=[]
b=input()
for i in b:
    a.append(i)
a.append("@")
z=''
y=[]
for i in range (len(a)):
    if (z=='') or (a[i] in z):
        z+=a[i]
    else:
        y.append((len(z),int(a[i-1])))
        z=''
        z+=a[i]
for i in  y:
    print(i,end=" ")