import threading
import time

def func():
    print("Atit")
    time.sleep(0.1)
    print("done")
x=threading.Thread(target=func)
x.start()
time.sleep(0.3)
print(threading.activeCount())
print("Atit is Hancy")
x.join()



print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

ls=[]
def count(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.1)

def count2(n):
    for i in range (1,n+1):
        ls.append(i)
        time.sleep(0.1)


x=threading.Thread(target=count,args=(4,))
x.start()
# x.join()
y=threading.Thread(target=count2,args=(4,))
y.start()
x.join()
y.join()

print(ls)