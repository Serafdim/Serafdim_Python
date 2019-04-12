#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random

def numb(st1, st2, st3):
        st = [st1, st2, st3]
        st_ram = [[],[],[]]
        i = 0
        while i < 3:
            for _ in range(5):
                while True:
                    r = random.randint(1, 90)
                    if r in st_ram[0] or r in st_ram[1] or r in st_ram[2]:
                        pass
                    else:
                        st_ram[i].append(r)
                        break
            st_ram[i] = sorted(st_ram[i])
            i += 1
        i = 0
        while i < 3:
            st_num = []
            while len(st_num) < 5:
                r = random.randrange(0,8)
                if r in st_num:
                    pass
                else:
                    st_num.append(r)
            st_num = sorted(st_num)
            ind = 0
            for _ in st_num:
                st[i][_] = st_ram[i][ind]
                ind +=1
            i += 1
        st[0] = st1
        st[1] = st2
        st[2] = st3
        return st1, st2 ,st3


def kegs():
    keg = []
    while len(keg) < 90:
        r = random.randrange(1, 91)
        if r in keg:
            pass
        else:
            keg.append(r)
    return keg


def prin_tic(st1, st2, st3, who):
    print(f'Карточка {who}')
    print(st1)
    print(st2)
    print(st3,'\n')


class Ticket_hum:
    st1 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    st2 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    st3 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    numb(st1, st2, st3)


    def find_num(self, num):
        self.num = num
        if num in self.st1:
            ind = 0
            for self.item in self.st1:
                if self.item == self.num:
                    self.st1[ind] = 'X'
                    return 'YES'
                ind += 1
        if num in self.st2:
            ind = 0
            for self.item in self.st2:
                if self.item == self.num:
                    self.st2[ind] = 'X'
                    return 'YES'
                ind += 1
        if num in self.st3:
            ind = 0
            for self.item in self.st3:
                if self.item == self.num:
                    self.st3[ind] = 'X'
                    return 'YES'
                ind += 1
        else:
            return 'NO'

    def win_or_no(self):
        k = 0
        for _ in self.st1:
            try:
                int(_)
            except ValueError:
                pass
            else:
                k += 1
                break
        for _ in self.st2:
            try:
                int(_)
            except ValueError:
                pass
            else:
                k += 1
                break
        for _ in self.st3:
            try:
                int(_)
            except ValueError:
                pass
            else:
                k += 1
                break
        if k == 0:
            return 'WIN'

class Ticket_comp(Ticket_hum):
    st1 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    st2 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    st3 = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    numb(st1, st2, st3)


tic_hum = Ticket_hum()
tic_comp = Ticket_comp()
keg = kegs()
keg = iter(keg)
while True:
    try:
        del_keg = next(keg)
        print(f'\nБоченок № {del_keg}\n')
        prin_tic(tic_hum.st1, tic_hum.st2, tic_hum.st3,'человека')
        prin_tic(tic_comp.st1, tic_comp.st2, tic_comp.st3, 'компьютера')
        while True:
            answer = input('Зачеркнуть число? Y/N: ')
            if answer != 'Y' and answer != 'N':
                print('\nВведите "Y" или "N"\n')
            else:
                break
        attempt = tic_hum.find_num(del_keg)
        if answer == 'Y' and attempt == "NO":
            print('Вы проиграли!')
            break
        if answer == 'N' and attempt == 'YES':
            print('Вы проиграли!')
            break
        tic_comp.find_num(del_keg)
        win_hum = tic_hum.win_or_no()
        win_comp = tic_comp.win_or_no()

    except StopIteration:
        print("Ничья")
        break
    if win_hum == 'WIN':
        print('Поздравляю, человек! Ты победил!')
        break
    elif win_comp == 'WIN':
        print('Очень жаль, но ты проиграл, человек!')
        break


