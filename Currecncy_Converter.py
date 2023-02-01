with open ('Currecncy.txt')as f:
    lines=f.readlines()
CurrecyDict={}
for Line in lines:
    NewLine=Line.split('  ')
    CurrecyDict[NewLine[0]]=NewLine[1]
[print(i) for i in CurrecyDict.keys()]
print("Enter the namme of currecny you want to convert Your NEPALI Rupee according to the above list")
Country=input("Which Country are you from, from the above list")
Amount=int(input("Enter how much amount  on \n"))
print(f'Your amount on {Country} is {Amount/ float(CurrecyDict[Country])}')
