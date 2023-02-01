from fractions import Fraction
from functools import reduce

def product(fracs):
    
  
    a=reduce(lambda x, y: x * y, fracs)
    y=Fraction(a)
    return y.numerator,y.denominator
    
    
        
    
    # print(y)

    
    # return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    # print(fracs)
    result = product(fracs)
    print(*result)

