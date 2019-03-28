
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    num = str(number)
    num_int = num[:num.find('.')]
    num_fraction = num[num.find('.') + 1:]
    while ndigits >= len(num_fraction):
    	num_fraction = num_fraction + '0'
    if int(num_fraction[ndigits:ndigits + 1]) >= 5:
    	num_fraction = str(int(num_fraction[:ndigits]) +1)
    	if ndigits < len(num_fraction):
    		num_int = str(int(num_int) + 1)
    		num_fraction = num_fraction[1:]
    else:
    	num_fraction = num_fraction[:ndigits]
    num = float(num_int + '.' + num_fraction)
    return num
    
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    num = str(ticket_number)
    if len(num) % 2 == 1:
    	return 'Вам не повезло'
    centr = int(len(num) / 2)
    begin = num[:centr]
    end = num[centr:]
    if sum(map(lambda x: int(x), list(begin))) == sum(map(lambda x: int(x), list(end))):
    	return 'Поздравляю! У вас счастливый билет'
    else:
    	return 'Вам не повезло'
    

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))



print('Здравствуйте! Добро пожаловать в решение easy ДЗ урока 3!')
while True:
    answer = input('Вы хотите посмотреть решение заданий? Y/N: ')
    if answer != 'Y' and answer != 'N':
        print('Дайте ответ Y или N')
    elif answer == 'N':
        print('Пока. Увидимся на следующем задании!')
        break
    elif answer == 'Y':
        number = int(input('какую задачу вы хотите увидеть? 1/2: '))

        if number == 1:
            print(my_round(2.1234567, 5))
            print(my_round(2.1999967, 5))
            print(my_round(2.9999967, 5))

        if number == 2:
            print(lucky_ticket(123006))
            print(lucky_ticket(12321))
            print(lucky_ticket(436751))