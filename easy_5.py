    
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import sys
import shutil

def mk_dirs(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'Директория {dir_name} укспешно создана')
    except FileExistsError:
        print(f'Директория {dir_path} уже существует\n')



def rm_dirs(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print(f'Директория {dir_name} успешно удалена')
    except FileNotFoundError:
        print(f'Директория {dir_path} не существует\n')



def dir_dirs(tipes = 'all'):
    dir_path = os.getcwd()
    all_dir = os.listdir(dir_path)
    dirs = []
    if tipes == 'all':
        print(f'содержимое директории {dir_path}:\n{all_dir}')
    elif tipes == 'dirs':
        for _ in all_dir:
            if os.path.isdir(_):
                dirs.append(_)
        print(f'папаки в директории{dir_path}:\n{dirs}')
    elif tipes == 'files':
        for _ in all_dir:
            if os.path.isfile(_):
                dirs.append(_)
        print(f'файлы в директории{dir_path}:\n{dirs}')


def copy_file():
    file_name = sys.argv[0]
    new_file_name = file_name + '_copy'
    if os.path.exists( new_file_name):
        print('Файл уже существует\n')
    else:
        shutil.copy(file_name, new_file_name)
        print(f'файл {new_file_name} успешно создан\n')


def program():
    while True:
        answer = input('\nПривет. хозяин! Какие дейтсвия вы хотите совнршить?\n'
              '1. создать директории dir_1 - dir_9 в папке, из которой запущен данный скрипт\n'
              '2. удалить директории dir_1 - dir_9 в папке\n'
              '3. отобразить директории в папке\n'
              '4. создать копию файла, из которого запущен данный скрипт\n'
              'если хотите выйти нажмите "q"\n'
              'Введите ответ 1/2/3/4/q: ')

        if answer == '1':
            i = 1
            while i < 10:
                dir_name = 'dir_' + str(i)
                mk_dirs(dir_name)
                i += 1
        elif answer == '2':
            i = 1
            while i < 10:
                dir_name = 'dir_' + str(i)
                rm_dirs(dir_name)
                i += 1
        elif answer == '3':
            dir_dirs('dirs')
        elif answer == '4':
            copy_file()
        elif answer == 'q':
            break
        else:
            print('Введите один из предложенных вариантов')
    
