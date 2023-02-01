a=[1,2,3,6,7,4,5]
for k in range (len(a)):
    swapped=False
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            swapped=True
    if swapped==False:
        break
print(a)
