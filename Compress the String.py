a='122'
def Compress(a):
    z=""
    count=0
    y=[]
    for i in a:
        if (z=="") or (i in z):
            z+=i
            count+=1
        elif i not in z:
            y.append(len(z))
            z=''
            z+=i
    print(y)
    
Compress(a)