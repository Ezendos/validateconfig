#!/usr/bin/python

# Описание:
# Проверка наличия указанной конфигурации
#
# Использование:
# validateconfig.py configfile
#
# спецификация конфигурации выглядит так:
# [[!]file|hash|reg|[!]user|[!]group] [args]
# примеры:
# file /usr/local/bin/sfx - файл существует
# hash 12384970347 /usr/local/bin/sfx - хеш файла
# !user bono - нет разрешенного пользователя "bono"
# group students - должна быть группа students

import sys
import pathlib


def vfile(args):  # file - проверка наличия имени файла
    print('kek')


def vhash(args):  # hash
    pass


def vuser(args):  # user
    pass


def vgroup(args):  # group
    pass


def errexit(entry):  # errexit - показать правильное использование и выйти
    print(f"invalid syntax in entry\n{entry}")
    print("usage: [!]file|hash|[!]user|[!]group [args]")
    sys.exit()


def get_args(entry):
    args = entry.split()
    if args[0] == '!':
        args[0] = False
    elif '!' in args[0]:
        args[0] = args[0][1:]
        args[0].strip()
        args.insert(0, False)
    else:
        args.insert(0, True)

    if args[1] in tasks.keys():  # проверка синтаксиса
        return args
    else:
        errexit(entry)


tasks = {
    'file': vfile,
    'hash': vhash,
    'user': vuser,
    'group': vgroup
}

config_path = pathlib.Path('config.txt')  # default configuration file

if len(sys.argv) > 1:
    config_path = pathlib.Path(sys.argv[1])


with open(config_path) as f:
    entries = f.readlines()
    for entry in entries:
        entry_args = get_args(entry)
        tasks[entry_args[1]](entry_args)
