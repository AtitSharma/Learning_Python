n="*"
s=" "
st="||"
st2="\/"
count=30
print(" *******************   MERRY CHRISTMAS PYTHON FAMILY ***************")
for i in range (1,30,2):
    print(s*count+n*i+s*count)
    count-=1
count=30
for j in range (3):
    print(s*count+st+s*count)
print(s*count+st2+s*count)
print(s*count+"=="+s*count)
print("-"*count*2)