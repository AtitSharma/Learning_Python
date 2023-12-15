import math

def reverse(num):
    ans=0
    while(num!=0):
        rem=num%10
        ans=ans*10+rem
        num=num//10
    return ans

def number_length(num):
    if num == 0:
        return 1 
    elif num < 0:
        num = -num 

    length = math.floor(math.log10(num)) + 1
    return length




def mul(num,ans=0,count=0,exp=0):
    if (num==0) and (number_length(ans)==1) and (number_length(exp)==1):
        finalans=ans+exp
        if number_length(finalans)!=1:
            mul(finalans,0,0,0)
        else:
            return finalans
    if num==0:
        ans+=exp
        return mul(ans,0,0,0)
    last_num=num%10
    
    num=num//10
   
    count+=1
    if count==2:
        exp*=last_num
        count=0
        pass
    else:
        exp+=last_num
        num=reverse(num)
        return mul(num,ans,count,exp)
    ans+=exp  
   
    return mul(num,ans,count,exp=0)






print(mul(0000))






