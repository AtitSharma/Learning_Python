import math
n=int(input())
fib=(1/math.sqrt(5))*(((1+math.sqrt(5))/2)**n)-(1/math.sqrt(5))*(((1-math.sqrt(5))/2)**n)
print(int((fib)))
