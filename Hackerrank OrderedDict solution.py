from collections import Counter
d=Counter()
for i in range (int(input())):
    name,space,price=input().rpartition(" ")
    
    d[name]=d[name]+int(price)
for i in d.items():
    print(*i)