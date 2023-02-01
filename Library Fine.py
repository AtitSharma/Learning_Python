D1=list(map(int,input().split()))
D2=list(map(int,input().split()))
y1=D1[2]
m1=D1[1]
d1=D1[0]
y2=D2[2]
m2=D2[1]
d2=D2[0]


def Fine(y1,y2,m1,m2,d1,d2):
    Fine=0
    if y1>y2:
        Fine= 10000
    elif y1==y2:
        if m1>m2:
            Fine=500*(m1-m2) 
        elif m1<m2:
            Fine=0  
        elif d1<d2:
            Fine=0        
        elif d1>d2 :
            Fine=15*(d1-d2)
            
        
    return Fine

        





print(Fine(y1,y2,m1,m2,d1,d2))