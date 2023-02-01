from functools import reduce
def add(x):
    return (x**2)


put=[1,2,3,4]
x=list(map(add,put))
print(sum(x))

def square(x):
    return x**2
print(list(map(square,put)))

x=list(map(lambda x:x**2,put))
print(x)
print(list(filter(lambda x: x > 2,put)))
print(list(map(lambda x: x > 2,put)))
print([i for i in put if i >2])
a=[1,2,3]
m=reduce(lambda x,y : x * y ,a)
print(m)


name=['ram','sham','hari','goapl']
marks=[10,20,30,100]
zipped=zip(name,marks)
print(dict(zipped))