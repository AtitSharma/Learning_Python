

def Combination(p,up):
    if up=="":
        print(p)
        return
    char=up[0]
    Combination(p,up[1:])
    Combination(p+char,up[1:])
    
Combination("",'abc')
