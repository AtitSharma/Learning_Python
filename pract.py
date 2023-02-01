from functools import reduce
a=[]
b=[]
ar=[]
n=int(input())
for i in range (n):
    name=input()
    marks=float(input())
    a.append(marks)
    b.append(name)

lowest_marks=reduce(min,a)
for numb in a:
    if lowest_marks<numb:
        ar.append(numb)
# print(a)
d=dict(zip(b,a))
# print(ar)
seconlowest_marks=reduce(min,ar)
# print(d[seconlowest_marks])

# print(d)
final_answer=[]
for i in d:
    if d[i]==seconlowest_marks:
        final_answer.append(i)
golo=sorted(final_answer)
for k in golo:
    print(k)
