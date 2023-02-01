def pad(p,up):
    if len(up)==0:
        print(p)
        return 
    digit=int(up[0])
    for i in range ((digit-1)*3,digit*3):
        ch=(chr(ord('a')+i))
        pad(p+ch,up=up[1:])

pad("",'23')