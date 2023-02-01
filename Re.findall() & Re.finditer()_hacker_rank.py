my_str=input()
vowels="AEIOUaeiou"
found_vow=""
count=0
z=[]
for i in my_str:
    if i in vowels:
        found_vow+=i
    if (i not in vowels) and len(found_vow)>1:
        z.append(found_vow)
        found_vow=''
    if i not in vowels:
        found_vow=""
if len(z)==0:
    print(-1)
else:
    for i in z:
        print(i)

