def quick_sort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    

    items_greater=[]
    items_smaller=[]


    for items in sequence:
        if items > pivot:
            items_greater.append(items)
        else:
            items_smaller.append(items)
    

    return quick_sort(items_smaller)+[pivot]+quick_sort(items_greater)
a=[1,2,5,5,5,5,5,53,53,53,5,213,5,25,25,23356,23,562,6]
print(quick_sort(a))