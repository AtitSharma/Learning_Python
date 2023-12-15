dl=int(input())
maths=int(input())
sci=int(input())
total=dl+maths+sci
percentage=(total/300)*100
if percentage >=40:
    if dl>40 and maths > 40 and sci >40:
        print(f"You are pass in all subject with {round(percentage)} %")
    else:
        print(f"You are fail with {round(percentage)} beacuse of low marks%")
else:
    print(f"You are fail because of low percentage i.e {round(percentage)}")
        


