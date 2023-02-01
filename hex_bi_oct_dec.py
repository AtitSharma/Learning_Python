def print_formatted(number):
    n=number
    m=len(str(bin(n))[2:])
    for i in range(1,n+1):
        print(str(i).rjust(m," "),oct(i)[2:].rjust(m," "),(hex(i).upper()[2:]).rjust(m," "),bin(i)[2:].rjust(m," "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)