a='{[()]}'
for _ in range (len(a)):
    a=a.replace("()",'')
    a=a.replace("[]",'')
    a=a.replace('{}','')
if len(a)==0:
    print("True")
else:
    print("False")

