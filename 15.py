lst1 = input()
lst2 = input()
lst3 = list(set(lst1)-set(lst2)) # Оставляем не одинаковые элементы
print(lst3)
