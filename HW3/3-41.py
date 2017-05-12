import string

a = string.ascii_lowercase
b = string.ascii_uppercase
d = string.digits
psw = list(input())
digit = False 
upper = False 
lower = False 
if len(psw) >= 8:
    for x in psw: 
        if x in d: 
            digit = True 
        if x in b: 
            upper = True 
        if x in a: 
            lower = True 
print(digit , upper , lower)
