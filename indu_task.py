a=[1,2,3]
b=[10,20,30]
#output
# [110,220,330]
print(list(map(lambda z,y: z+y,list(map(lambda x:x*100,a)),b)))
print([i*100+j for i,j in list(zip(a,b))])
print(list(map(int,[str(i)+str(j) for i,j in list(zip(a,b))])))
# print([i[0]+i[1] for i in map(lambda x, y: (str(x),str(y)), b, a)])
