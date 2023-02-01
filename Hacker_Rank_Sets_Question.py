a=int(input())
First_Set=set(map(int,input().split()))
for i in range (int(input())):
    xyz=list(map(str,input().split()))
    Second_Set=set(map(int,input().split()))
    if xyz[0]=="intersection_update":
        First_Set.intersection_update(Second_Set)
    elif xyz[0]=="update":
        First_Set.update(Second_Set)
    elif xyz[0]=="symmetric_difference_update":
        First_Set.symmetric_difference_update(Second_Set)
    elif xyz[0]=="difference_update":
        First_Set.difference_update(Second_Set)
    
print(sum(First_Set))