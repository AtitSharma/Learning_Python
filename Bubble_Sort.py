def BubbleSort(List):
    size=len(List)
    for k in range (size-1):
        for i in range (size-1-k):
            if List[i] > List[i+1]:
                tmp=List[i]
                List[i]=List[i+1]
                List[i+1]=tmp
    return List

List=[0,101,1,444,2,3,5,7,10,8]
a=BubbleSort(List)
print(a)