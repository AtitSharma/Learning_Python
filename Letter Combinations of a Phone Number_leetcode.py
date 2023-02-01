from itertools import combinations,permutations, product
digits='234'
oup='["ad","ae","af","bd","be","bf","cd","ce","cf"]'

Mydict={
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz'
}

x=[]
for i in digits:
    x.append([j for j in Mydict[i]])
My_List=[]
m=list(product(*x))
for i in m:
    My_List.append(''.join(i))
print(My_List)



