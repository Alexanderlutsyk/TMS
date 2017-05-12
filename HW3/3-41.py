lst_seq = input() 
print(map(chr, range(ord(lst_seq))))
psw = list(input())
digit = False 
upper = False 
lower = False 
if len(psw) >= 8:
    for x in psw: 
        if x in lst_seq('0','9'): 
            digit = True 
        if x in lst_seq('A', 'Z'): 
            upper = True 
        if x in lst_seq('a', 'z'): 
            lower = True 
print(digit , upper , lower)
