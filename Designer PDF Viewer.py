from functools import reduce
Alphabet=list(map(chr, range(97, 123)))
Mylist=list(map(int,input().split()))
my_dict=zip(Alphabet,Mylist)
my_dict=(dict(my_dict))
my_str=input()
z=[]
for i in my_str:
    z.append(my_dict[i])
print(len(z)*1*reduce(max,z))