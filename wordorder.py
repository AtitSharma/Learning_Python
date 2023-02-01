dict={}
for i in range (int(input())):
    a=input()
    if a in dict:
        dict[a]+=1
    else:
        dict[a]=1
print(len(dict))
for i in dict:
    print(dict[i],end=" ")