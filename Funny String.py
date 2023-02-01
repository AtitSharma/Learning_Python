for i in range (int(input())):
    s=input()
    my_list=[ord(j) for j in s]
    reverse_list=my_list[::-1]
    my_list_new_after_sub=[]
    reverse_new_list_after_sub=[]
    for k in range (len(my_list)-1):
        my_list_new_after_sub.append(abs(my_list[k+1]-my_list[k]))
    for x in range (len(reverse_list)-1):
        reverse_new_list_after_sub.append(abs(reverse_list[x+1]-reverse_list[x]))
    if my_list_new_after_sub==reverse_new_list_after_sub:
        print("Funny")
    else:
        print("Not Funny")
