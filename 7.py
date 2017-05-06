import string 

print('Введите пароль')
a = str(input())
j = ()
h = ()
l = ()
m =() 
k = len(a)
upper  = set(string.ascii_uppercase)
lower  = set(string.ascii_lowercase)
digits = set(string.digits) 
punctuation = set(string.punctuation)
if not 6 <= k <= 16:
    k = ('длина пароля не соответствует') 
if not upper in (a):
    j ='нет заглавных символов'
if not lower in (a):
    h ='нет строчных символов'
if not digits in (a):
    l ='отсутствуют цифры'
if not punctuation in (a):
    m ='отсутствуют знаки припинания'
print(k,j,h,l,m)    
