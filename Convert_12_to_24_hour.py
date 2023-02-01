
def TimeConverter(a):
    if a[:2]=='12' and  a[-2]=='A':
        return "00"+a[2:-2]
    elif a[-2]=="A":
        return a[:-2]
    elif a[-2] == "P" and a[:2] == "12":
        return a[:-2]
    else:
        return str(int(a[:2]) + 12) + a[2:8]


a=str(input())
print(TimeConverter(a))

