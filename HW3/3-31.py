stask = ['сделать домашку','отрегулирвать впрыск','повесить молдинг']
sstatus = ['в работе','отложено','выполнено'] # создаем спсиски  заданий и состояние 


for i in stask:
	for i in range(len(stask)):
		print('{}      {}'.format(stask[i],sstatus[i]))

	print('поменять статус? (y/n)')
	q = input()
	if q == 'y':
		print('у какого задания хочешь поменять(0..n)')
		x = int(input())
		print('введи статус (в работе\ отложено\ выполнено )')
		z = input()
		if  x ==0:
			sstatus[0] = z
		elif x ==1:
			sstatus[1] = z
		elif x ==2:
			sstatus[2] = z	
		elif x ==3:
			sstatus[3] = z
	if  q == 'n':
		pass
	print('хочешь добавить или удалить задание? (введи 1- добавить, 2- удалить, 3-пропустить)')
	f = int(input())
	if  f == 1:
		print('введи задание')
		h = input()
		print('введи состояние')
		j = input()
		stask.insert(len(stask)+1,h)
		sstatus.insert(len(sstatus)+1,j)
	if f ==2:
		print('введи номер задания которое можно удалить (0...n)')
		l = int(input())
		stask.pop(l)
		sstatus.pop(l)
	else:
		pass
		
	
 
