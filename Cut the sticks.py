a=int(input())
arr=list(map(int,input().split()))
print(len(arr))
while True:                 
    arr=[i for i in arr if i!= min(arr)]
    if len(arr)==0:
        break
    else:
        print(len(arr))
