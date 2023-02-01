li=[1,2,3,4,5,6]
def func(x):
    return x**x
my=list(map(func,li))
print(my)
print(list(func(x) for x in li if x%2==0 ))
def sqr(x):
    return x*x
print(list(map(sqr,li)))
print(list(map(lambda x:x*x,li)))


#FILTER FUNCTION

def Odd(x):
    return x%2!=0
def Add7(x):
    return x+7

print(list(filter(Odd,li)))
x=[i for i in li if i%2 ==0]
y=list(map(Add7,filter(Odd,li)))
print(y)
print(list(map(lambda x :(Add7(x))**2,li)))



####   Lambda


AddFunc=lambda x:x+9
print(AddFunc(10))


Func=lambda x,y:x**2+y**2
print(Func(10,11))


a=[(1,2),(3,4),(7,1),(6,7)]
a.sort(key=(lambda x:x[1]))
print(a)



