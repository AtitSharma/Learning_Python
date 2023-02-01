Start_Page=int(input())
Destination=int(input())
Book=[]
count=0
one=1
for i in range (0,Start_Page+1):
    Book.append((i+count,i+one))
    one+=1
    count+=1
print(Book)
