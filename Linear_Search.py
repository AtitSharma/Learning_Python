pos=-1
def Search(List,n):
    
    for i in range (len(List)):
        if List[i]==n:
            globals() ['pos']=i
            return True
    return False

List=[1,2,3,4,5,7]
n=7
if Search(List,n):
    print("Found at ",pos+1)
else:
    print("Not Found")

