matrix = [[1,2,3],[4,5,6],[7,8,9]]
z=[]
for j in range (len(matrix)):
    x=[item[j] for item in matrix ]
    z.append(x)
m=[]
for i in z:
    xx=i[::-1]
    m.append(xx)
print(m)
