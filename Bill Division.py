a=list(map(int,input().split()))
Foods=list(map(int,input().split()))
Anna_Paid=int(input())
Foods.pop(a[1])
Foods_Amount=sum(Foods)
Bill_To_Paid_By_Anna=Foods_Amount//2
if Bill_To_Paid_By_Anna==Anna_Paid:
    print("Bon Appetit")
elif Bill_To_Paid_By_Anna<Foods_Amount:
    print(Anna_Paid-Bill_To_Paid_By_Anna)


