

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	list_f = [1, 1]
	i = 2
	while i < m:
		list_f.append(list_f[i - 2] + list_f[i - 1])
		i += 1
	return list_f[n - 1:]




# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	finish_list = []
	finish_list.insert(0,origin_list[0])
	i = 1
	while i < len(origin_list):
		k = 0
		while k < len(finish_list):
			if origin_list[i] < finish_list[k]:
				finish_list.insert(k, origin_list[i])
				break
			elif k == len(finish_list) - 1:
				finish_list.append(origin_list[i])
				k += 1
			k += 1
		i += 1
	print(finish_list)




# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter (cond, filtr_list):
	ready_lisr = []
	for item in filtr_list:
		if cond(item) == True:
			ready_lisr.append(item)
	return ready_lisr




# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def coordinates(point):
	x = int(input('Введите координату x точки ' + point + ': '))
	y = int(input('Введите координату y точки ' + point + ': '))
	return [x, y]

def centr(point1, point2):
	cent_x = (point1[0] + point2[0]) / 2
	cent_y = (point1[1] + point2[1]) / 2
	return [cent_x, cent_y]

print('Здравствуйте! Добро пожаловать в решение normal ДЗ урока 3!')
while True:
	answer = input('Вы хотите посмотреть решение заданий? Y/N: ')
	if answer != 'Y' and answer != 'N':
		print('Дайте ответ Y или N')
	elif answer == 'N':
		print('Пока. Увидимся на следующем задании!')
		break
	elif answer == 'Y':
		number = int(input('какую задачу вы хотите увидеть? 1/2/3/4: '))



		if number == 1:
			n = int(input('Введите с какого элемета хотите начать ряд: '))
			m = int(input('Введите на каком элемете хотите закончить ряд: '))
			print(fibonacci(n, m))


		if number == 2:
			sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

		if number == 3:
			f = [1, 2, 4, 0, 1, 3, 5, 6]
			print(my_filter(lambda x: x > 1 and x < 5, f))

		if number == 4:
			A1 = coordinates('A1')
			A2 = coordinates('A2')
			A3 = coordinates('A3')
			A4 = coordinates('A4')

			center_A1A3 = centr(A1, A3)
			center_A2A4 = centr(A2, A4)
			if center_A1A3[0] == center_A2A4[0] and center_A1A3[1] == center_A2A4[1]:
				print (f'точки с координатами А1:{A1}, A2:{A2}, A3:{A3}, A4:{A4} являются вершинами параллелограмма')
			else:
				print (f'точки с координатами А1:{A1}, A2:{A2}, A3:{A3}, A4:{A4} не являются вершинами параллелограмма')
