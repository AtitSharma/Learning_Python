from collections import Counter
a="aaabaabbbbccc"
My_counter=Counter(a)
print(My_counter)
print(My_counter.keys())
print(My_counter.values())
print(My_counter.most_common(2))
print(My_counter.most_common(2)[0][1])
print(My_counter.elements())
print(list(My_counter.elements()))

from collections import OrderedDict
My_dict=OrderedDict()
My_dict['a']=10
My_dict['b']=10
My_dict['c']=10
My_dict['d']=10
My_dict['d']=10
print(My_dict)

from collections import defaultdict
d=defaultdict(int) #can put list,tuple,float ,int
d['a']=10
d['b']=20
print(d['a'])
print(d['c'])



d=[]
z=list(map(int,input().split()))
d=defaultdict(list)
List=[]
for i in range (z[0]):
    liSt=input()
    d[liSt].append(i+1)
for i in range (z[1]):
    List.append(input())
for i in List:
    if i in d:
        print(" ".join(map(str,d[i]) ))
    else:
        print(-1)