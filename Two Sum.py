from itertools import combinations
Input=eval(input())
Target=int(input())
Input=[i for i in Input if i<=Target]
z=[list(combinations(Input,i)) for i in range (1,len(Input)+1)]
l=0
kam=[]
for i in z:
    for j in i:
        if sum(j)==Target:
            for k in j:
                v=(Input.index(k)+l)
                kam.append(v)
                Input.remove(k)
                l+=1
y=str(kam).replace(" ","")
print(y)
