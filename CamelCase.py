
a=input()
a+='X'
my_str=''
count=0
for i in a:
    if i.isupper():
        # print(my_str)
        count+=1
        my_str=''
        my_str+=i
    else:
        my_str+=i
print(count)
