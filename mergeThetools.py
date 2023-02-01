
def merge_the_tools(string, k):
    empty=""
    count=0
    for i in string:
        if i not in empty:
            empty+=i
        count+=1
        if count==k:
            print(empty)
            count=0
            empty=""
        






if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
            





