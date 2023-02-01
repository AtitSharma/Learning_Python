import random
print("Guess the number between 0 to 100")
a=random.randint(0,100)
count=1
while True:
    num=int(input())
    if num>a:
        print("Choose the less number")
    elif num < a:
        print("Choose a greater number")
    else:
        print(f"You choosed the correct number in {count} attempt")
        break
    count+=1
