import re
a="aaadaa"
m = re.search(r'a',a)
print(m.start())
print(m.end())
m=re.findall("aa",a)
print(m)
