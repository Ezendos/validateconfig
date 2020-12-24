#!/usr/bin/python3

# Описание:
# Проверка наличия указанной конфигурации
#
# Использование:
# validateconfig.py [путь к файлу конфигурации]
#
# спецификация конфигурации:
# [[!]file|hash|reg|[!]user|[!]group] [args]
# примеры:
# file /usr/local/bin/sfx - файл существует
# hash 12384970347 /usr/local/bin/sfx - sha1 хеш файла
# !user bono - не должно быть пользователя "bono"
# group students - должна быть группа students

import sys
import pathlib  # работа с путями
import pwd      # доступ к базе данных учетных записей пользователей *nix
import grp      # доступ к базе данных групп Unix
import hashlib  # работа с хеш-функциями


# file проверка наличия имени файла
def vfile(args):
    fname = pathlib.Path(args[2])
    if args[0] is True:
        if fname.is_file():
            return False
        else:
            return True
    else:
        if fname.is_file():
            return True
        else:
            return False


# hash проверка хеша файла
def vhash(args):
    a = hashlib.sha1()
    with open(args[3], "rb") as fh:
        data = fh.read()
        a.update(data)
    if a.hexdigest() == args[2]:
        return True
    else:
        return False


# user проверка наличия пользователя
def vuser(args):
    if args[0] is True:
        try:
            pwd.getpwnam(args[2])
            return False
        except KeyError:
            return True
    else:
        try:
            pwd.getpwnam(args[2])
            return True
        except KeyError:
            return False


# group проверка наличия группы
def vgroup(args):
    if args[0] is True:
        try:
            grp.getgrnam(args[2])
            return False
        except KeyError:
            return True
    else:
        try:
            grp.getgrnam(args[2])
            return True
        except KeyError:
            return False


# errexit показать правильное использование и выйти
def errexit(entry, argnum=0):
    print(f"invalid syntax in entry\n{entry.strip()}")
    if argnum:  # ошибка в количестве аргументов
        print(f"key takes {argnum} arguments")
    else:      # ошибка в ключевом аргументе
        print("usage: [!]file|hash|[!]user|[!]group [args]")
    sys.exit()


# Функция обработки строк конфигурационного файла
# Возвращяет список вида:
#     [флаг_инверсии, ключевое_слово, аргумент1, аргумент2 ...]
# Вхождения начинающиеся с "#" игнорируются
def get_args(entry):
    if entry[:1] == '#':
        return
    args = entry.split()
    if args:
        if args[0] == '!':  # обработка параметра инверсии
            args[0] = True
        elif '!' in args[0]:
            args[0] = args[0][1:]
            args[0].strip()
            args.insert(0, True)
        else:
            args.insert(0, False)
        # проверка синтаксиса
        # соответствие ключевого слова
        if args[1] not in tasks.keys():
            errexit(entry)
        # соответствие количества аргументов
        if len(args) != tasks[args[1]][1] + 1:
            errexit(entry, tasks[args[1]][1])
        return(args)


# Словарь задач по сравнению конфигураций
# Формат:
#     'ключевое_слово' : (функция, количество_аргументов)
# ключевое_слово - имя проверяемой конфигурации
# прим. количество аргументов не включает "!"
tasks = {
    'file': (vfile, 2),
    'hash': (vhash, 3),
    'user': (vuser, 2),
    'group': (vgroup, 2),
}

# config.txt - путь к конфигурационному файлу по умолчанию
config_path = pathlib.Path('config.txt')

# Получение пути к файлу конфигурации из аргумента командной строки
if len(sys.argv) > 1:
    config_path = pathlib.Path(sys.argv[1])

with open(config_path) as f:
    line = 0  # счетчик линий
    entries = f.readlines()  # считываем все строки
    for entry in entries:
        line += 1
        entry_args = get_args(entry)  # получение аргументов
        if entry_args:
            try:
                # Проверка на соответствие конфигурации
                # текущим параметрам системы
                if not(tasks[entry_args[1]][0](entry_args)):
                    # Сообщение о непрохождении проверки
                    print(f"Fail in line {line}: {entry.strip()}")
            except Exception as e:
                # Сообщение о возникновении исключения при обработке строки
                print(f"Caught exception in line {line}: {entry.strip()}\n", e)
