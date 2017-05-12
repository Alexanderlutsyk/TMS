
import random


viselica = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

mist = len(viselica) - 1
slova = ("ГОВНОКОД", "НУБ", "ПРОГРАММА", "КОДЕР", "ЛОШАРА")


word = random.choice(slova)   
so_far = "-" * len(word)      
wrong = 0                     
used = []                     


print("Виселица")

while wrong < mist and so_far != word:
    print(HANGMAN[wrong])
    print("\nнапиши букву:\n", used)
    print("\nслово:\n", so_far)

    guess = input("\n\nвведи свою букву: ")
    guess = guess.upper()
    
    while guess in used:
        print("твоя буква ", guess)
        guess = input("введи : ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\n да", guess, "есть в слове")

        
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]              
        so_far = new

    else:
        print("\nИзвини", guess, "нет в слове")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nты повешен")
else:
    print("\nты сделал это!")
    
print("\nслово", word)

input("\n\nнажми enter и уходи.")
