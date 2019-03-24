
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
import random



print('Здравствуйте! Добро пожаловать в решение easy ДЗ урока 2!')
while True:
    answer = input('Вы хотите посмотреть решение заданий? Y/N: ')
    if answer != 'Y' and answer != 'N':
        print('Дайте ответ Y или N')
    elif answer == 'N':
        print('Пока. Увидимся на следующем задании!')
        break
    elif answer == 'Y':
        number = int(input('какую задачу вы хотите увидеть? 1/2/3: '))

        if number == 1:
            fruits = []

            while True:
                qest = input('Хотите добавить фрукты в список? Y/N: ')
                if qest == 'N':
                    break
                elif qest != 'N' and qest != 'Y':
                    print('Введите Y или N')
                elif qest == 'Y':
                    while True:
                        count_fruits = input('Сколько фруктов вы хотитк добавить? Количество фруктов: ')
                        if False == count_fruits.isdigit():
                            print('Количество фруктов это целое число!')
                        else:
                            count_fruits = int(count_fruits)
                            break
                    i = 0
                    while i < count_fruits:
                        fruits.append(input('Введите назвыание фрукта: '))
                        i += 1

            i = 1
            for pr in fruits:
                print(f'{i}.{pr:>10}')
                i += 1

        if number == 2:
            list1 = []
            list2 = []
            count_index1 = int(random.randrange(5, 10))
            count_index2 = int(random.randrange(5, 10))
            i = 0

            while i < count_index1:
                list1.append((random.randrange(0, 10)))
                i += 1
            i = 0
            while i < count_index2:
                list2.append((random.randrange(0, 10)))
                i +=1
            print(f'Первый список: {list1}')
            print(f'Второй список: {list2}')

            i = 0
            while i < len(list1):
                for elem2 in list2:
                    if list1[i] == elem2:
                        list1.pop(i)
                        i -= 1
                        break
                i += 1


            print(f'Первый список: {list1}')
            print(f'Второй список: {list2}')


        if number == 3:
            list1 = []
            list2 = []
            count_index1 = int(random.randrange(10, 15))
            i = 0

            while i < count_index1:
                list1.append((random.randrange(0, 10)))
                i += 1
            print(f'Исходный список: {list1}')

            i = 0
            for elem in list1:
                if (elem % 2) == 0:
                    list2.append(elem / 4)
                else:
                    list2.append(elem * 2)

            print(f'Полученный список: {list2}')