

def decorator(func):
    
    def wrapper(x,y):
        print("Hello")
        print(x+y)
    return wrapper
    
    
    
    






@decorator
def add(x,y):
    return x+y

add(1,2)
