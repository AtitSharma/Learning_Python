def fact(n):
    if n==0:
        return 1
    print(n)
    fact(n-1)
    print(n)

fact(20)

# def factReverse(n):
#     if n==0:
#         return 
#     factReverse(n-1)
#     print(n)

# factReverse(20)



def Sum(n):
    if n<=1:
        return n
    return n + Sum(n-1)
print(Sum(3))