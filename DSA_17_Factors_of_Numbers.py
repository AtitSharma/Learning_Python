import math

def factors(n):
    My_List=[]
    for i in range (1,int(math.sqrt(n))+1):
        if n%i==0:
            if n//i==i:  # it is done to avoid multiple  same numbers in the array. IF 36 is given then 6x6=36 and it would print 6 ,2 times
                My_List.append(i)
            else:
                My_List.append(i)
                My_List.append(n//i)
    My_List.sort()
    for k in (My_List):
        print(k,end=" ")

factors(36)
        