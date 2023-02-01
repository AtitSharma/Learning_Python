elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
def BubbleSort(elements,key='name'):
    size=len(elements)-1
    for j in range (size):
        for i in range (size):
            if elements[i][key] > elements[i+1][key]:
                temp=elements[i]
                elements[i]=elements[i+1]
                elements[i+1]=temp
    return elements
print(BubbleSort(elements,key='name'))





