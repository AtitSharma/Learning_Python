arr=["dog","racecar","car"]
def Long(arr):
    cr=''
    if len(arr)==0:
        return cr
    if len(arr)==1:
        return arr[0]
    for i in range (0,len(min(arr))):
        current=arr[0][i]
        for j in range (0,len(arr)):
            if arr[j][i]!=current:
                return cr
        cr+=current
    return cr
print(Long(arr))
