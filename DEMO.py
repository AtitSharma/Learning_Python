
num=int(input())
Pass=input()
Ans=0

def lowercase(Pass):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    z=0
    for i in Pass:
        if i in lower_case:
            z+=1
    if z==0:
        return True

def uppercase(Pass):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    z=0
    for i in Pass:
        if i in upper_case:
            z+=1
    if z==0:
        return True

def special(Pass):
    special_characters = "!@#$%^&*()-+"
    z=0
    for i in Pass:
        if i in special_characters:
            z+=1
    if z==0:
        return True

def number(Pass):
    numbers = "0123456789"
    z=0
    for i in Pass:
        if i in numbers:
            z+=1
    if z==0:
        return True

if lowercase(Pass):
    Ans+=1
if uppercase(Pass):
    Ans+=1
if special(Pass):
    Ans+=1
if number(Pass):
    Ans+=1

