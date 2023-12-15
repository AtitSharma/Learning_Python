a=[1,2,3,4,5,"9.9",9]
x=list(filter(lambda b : b.isalnum(),map(str,a)))
print(x)
    