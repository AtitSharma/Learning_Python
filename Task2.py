import time

def timit(func):
    def timeit_wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f'Time taken by {func.__name__} is: {t2-t1}')
    return timeit_wrapper
        


@timit
def miss():
    new_list=[5,6,7,1,2,3,4,9,10]
    n = len(new_list)+1
    s1 = sum(new_list)
    s2 = n * (n+1)//2 # O(1)
    print(f"missing number is: {s2-s1}")



@timit
def miss1():
    new_list=[5,6,7,1,2,3,4,8,10]
    new_list.sort()
    for i in range(len(new_list)-1):
        if new_list[i]!=i+1:
            print(i+1)
        else:
            print(new_list[i],"index",i)


# miss()

miss1()
