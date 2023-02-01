a=int(input())
sequence=[int(input()) for i in range (a)]
def Quick_Sort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    
    smaller_than=[]
    greater_than=[]
     
    for i in sequence:
        if i>pivot:
            greater_than.append(i)
        else:
            smaller_than.append(i)
    
    return Quick_Sort(smaller_than)+[pivot]+Quick_Sort(greater_than)

    
x=Quick_Sort(sequence)
for i in x:
    print(i)
