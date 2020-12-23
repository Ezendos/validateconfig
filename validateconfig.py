#!/usr/bin/python3

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
    return True


def vhash(args):  # hash
    return True


def vuser(args):  # user
    return True


def vgroup(args):  # group
    return True


def errexit(entry):  # errexit - показать правильное использование и выйти
    print(f"invalid syntax in entry\n{entry.strip()}")
    print("usage: [!]file|hash|[!]user|[!]group [args]")
    sys.exit()


def get_args(entry):
    if entry[:1] == '#':  # комментарии пропускаются
        return

    args = entry.split()
    if args:
        if args[0] == '!':
            args[0] = True
        elif '!' in args[0]:
            args[0] = args[0][1:]
            args[0].strip()
            args.insert(0, True)
        else:
            args.insert(0, False)

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

config_path = pathlib.Path('config.txt')  # конфигурационный файл по-умолчанию

if len(sys.argv) > 1:
    config_path = pathlib.Path(sys.argv[1])


with open(config_path) as f:
    line = 0
    entries = f.readlines()
    for entry in entries:
        line += 1
        entry_args = get_args(entry)
        if entry_args:
            if tasks[entry_args[1]](entry_args):
                print(f"Fault in line {line}: {entry.strip()}")
