import math
x=input()
a=len(x)
word=0
for i in range (a):
    if math.sqrt(a)<i:
        word+=i
        break
steps=int((math.sqrt(a)))
print(word)
print(steps)
z=[]
for i in range (steps):
    print(x[i::steps],end=" ")












    

