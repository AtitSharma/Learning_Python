import re
for i in range (int(input())):
    try:
        a=re.compile(input())
        if a:
            print("True")
    except re.error:
        print('False')
