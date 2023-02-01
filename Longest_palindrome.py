a="cbbd"
stri=''
s=0
e=len(a)-1
count=0
y=1
while True:
    for i in a:
        stri+=i
        if len(stri)>1:
            if stri==stri[::-1]:
                print(stri)
                break
    count+=1
    if count==e:
        stri=''
        a=a[y:]
        print(a)
        y+=1
        count=0




