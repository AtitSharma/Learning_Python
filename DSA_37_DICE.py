def Dice(p,target):
    if target==0:
        print(p)
        return
    for i in range (1,7):
        if i <= target:
            Dice(p+str(i),target-i)
Dice('',4)