a = input()
b = input()
result = []
 
for i in b:
    if i in a:
        result.append(i)
if (len(result)) > 0:
	print('есть общие элементы их количество = ', len(result))
else:
	print('нет общих элементов')
