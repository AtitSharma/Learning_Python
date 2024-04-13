def square(num,pow):
    if pow <=1:
        return num
    return num * square(num=num,pow=pow-1)

print(square(2,3))