import re
import email.utils

def checker(y):
    pattern=r"^[a-zA-Z0-9]+.+@[a-zA-Z]+\.[a-z]{3}$"
    pattern2=r"^[a-zA-Z0-9]+.+@[a-zA-Z]+\.[a-z]{1}$"
    pattern3=r"^[a-zA-Z0-9]+.+@[a-zA-Z]+\.[a-z]{2}$"

    if re.match(pattern,y):
        return  email.utils.formataddr((a[0], y))
    elif re.match(pattern2,y):
        return  email.utils.formataddr((a[0], y))
    elif re.match(pattern3,y):
        return  email.utils.formataddr((a[0], y))
n=int(input())
for i in range (n):
    y=input()
    a= email.utils.parseaddr(y)

    z=(checker(a[1]))
    if z==None:
        pass
    else:
        print(z)


# import email.utils
# print(type( email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')))
# # print (email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))




