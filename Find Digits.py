for i in range (int(input())):
    count=0
    a=input()
    for j in a:
        try:
            if int(a)%int(j)==0:
                count+=1
        except:
            pass
    print(count)
