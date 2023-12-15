n = 123



def sum_of_digits(n):
    digit = n
    sum = 0
    while(digit>0):
        rem = digit%10
        sum*=rem
        digit = digit//10
    return sum


print(sum_of_digits(n))







    

    