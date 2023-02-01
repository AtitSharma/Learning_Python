from collections import deque
s=deque()
a='We will conquere COVID-19'
for i in a:
    s.append(i)
m=''
for i in range (len(s)):
    rs=s.pop()
    m+=rs
print(m)

