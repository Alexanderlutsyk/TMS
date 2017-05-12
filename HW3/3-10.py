s = input()
j=len(s)
i = 0
k = 0
for letter in s:
    if letter.isalpha():
        i+=1
    else:
        k +=1
print( 'длина строки =',j)
print('число цифр =',k,'число букв =',i,)    
