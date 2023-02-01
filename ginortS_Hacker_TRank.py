New_List=[]
Final_List=[]
a=input()
for i in a:
    New_List.append(i)
New_List.sort()
# print(New_List)
integers=[]
s = ''.join(x for x in New_List if x.isdigit())
# print(str(s))
for i in s:
    integers.append(i)
# print(integers)
List_Of_CAPITAL_Letters=[]
Capital_letters=''.join(x for x in New_List if x.isupper())
# print(Capital_letters)
for i in Capital_letters:
    List_Of_CAPITAL_Letters.append(i)
# print(List_Of_CAPITAL_Letters)
for i in integers:
    if i  in New_List:
        New_List.remove(i)
for i in Capital_letters:
    if i  in New_List:
        New_List.remove(i)
List_Of_CAPITAL_Letters.sort()
# print(New_List)
New_list_Of_integers=[]
integers_Integer = ' '.join(x for x in integers if x.isdigit())
hello=(integers_Integer).split()
# print(hello)
xyz=[ int(i)for i in hello]
# print(xyz)
odd_numbers=[i for i in xyz if i%2]
odd_numbers.sort()
# print(odd_numbers)
even_numbers=[i for i in xyz if i%2==False]
even_numbers.sort()
# print(even_numbers)
for i in List_Of_CAPITAL_Letters:
    New_List.append(i)
for i in odd_numbers:
    New_List.append(i)
for i in even_numbers:
    New_List.append(i)
# print(New_List)
for i in New_List:
    print(i,end="")
