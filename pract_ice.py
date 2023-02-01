


# a=[(1,2,5),(1,2,4),(5,6,1)]
# output=list(map(lambda array: sum(map(lambda x : x**2, array)),a))
# print(output)



a="AABCAAADA"
string=''
k=3
count=0
for i in a:
    if i  not in  string:
        string+=i
    count+=1
    if (count==k):
        print(string)
        string=""
        count=0

