    
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os
import sys
import shutil

print('sys.argv = ', sys.argv)
conf_path = os.path.join(os.getcwd(),'hardConfig.txt')
if os.path.exists( conf_path):
    hard_conf = open(conf_path, 'r')
    conf_list = hard_conf.readlines()
    if conf_list:
        all_path = conf_list[0]
        print(all_path)
        hard_conf.close()
    else:
        all_path = os.getcwd()
else:
    all_path = os.getcwd()





def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> создать копию указанного файла")
    print("rm <file_name> удалить указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(all_path, dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))



def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(all_path, file_name)
    new_file_path = file_path + '_copy'
    try:
        shutil.copy(file_path, new_file_path)
        print(f'файл {new_file_path} успешно создан\n')
    except FileNotFoundError:
        print('Файла с таким именем нет')
    if os.path.exists( new_file_path):
        print('Файл уже существует\n')



def rm_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(all_path, file_name)
    answer = input(f'Вы точно хотите удалить файл{file_name}? Y/N: ')
    if answer == 'Y':
        try:
            os.remove(file_path)
            print(f'Файл {file_name} успешно удален')
        except FileNotFoundError:
            print(f'Файла {file_name} не существует\n')
    elif answer == 'N':
        print('Удаление отменено')
    else:
        print('Ответте Y или N')

def full_path():
    print('Полный путь к текущей дериктории: ', os.path.abspath(all_path))

def cd():
    if not new_path:
        print("Необходимо указать путь вторым параметром")
        return
    try:
        new_dir_path = os.path.join(new_path)
        all_path = os.chdir(new_dir_path)
        hard_conf = open(conf_path, 'w+')
        all_path = hard_conf.write(new_dir_path)
        print(f'Переходв в {new_dir_path} произошел успешно')
        hard_conf.close()
    except FileNotFoundError:
        print('Такой дериктории нет')

def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp":copy_file,
    "rm":rm_file,
    "cd":cd,
    "ls":full_path,
    "ping": ping,
    }

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    new_path = os.path.join(all_path,sys.argv[2])
    new_path = os.path.abspath(new_path)
except IndexError:
    new_path = None


try:
    key = sys.argv[1]
except IndexError:
    key = None
try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")