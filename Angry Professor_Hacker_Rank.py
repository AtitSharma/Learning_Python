for i in range (int(input())):
    Required_S=list(map(int,input().split()))
    Came_Student=list(map(int,input().split()))
    List=[]
    for i in Came_Student:
        if i<=0:
            List.append(i)
    if len(List)>=Required_S[-1]:
        print("No")
    else:
        print("Yes")
    
