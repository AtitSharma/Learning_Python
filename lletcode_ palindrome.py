# The idea is correct but syntax eoor in leetcode


words = ["abc","car","ada","racecar","cool"]
y=''

def Palindrome(stri):
    s=0
    e=len(stri)-1
    while s<e:
        if stri[s]==stri[e]:
            s+=1
            e-=1
        else:
            return False
    if s==e:
        return True
    else:
        return False

for i in words:
    if Palindrome(i):
        print(i)
        y+='1'
        break
    else:
        y+=''
if len(y)==0:
    print("")




