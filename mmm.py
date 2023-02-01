a={'ram':'200','sam':'2000','kam':'100','dam':'1000'}
dam=[]
for i in a:
    dam.append((i,a[i]))
dam.sort(key=lambda x:x[0])
Dict={}
for i in dam:
    Dict[i[0]]=i[1]
print(Dict)
