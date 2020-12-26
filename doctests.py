import pathlib
import doctest
import hashlib
import pwd
import grp


def vfile(args):  # file - проверка наличия имени файла
    """
    файла file в системе - нет
    файл config.txt - существует
    >>> vfile([True, 'file', 'file']) #файла file не является файлом
    True
    >>> vfile([False, 'file', 'file']) #файла file является файлом
    False
    >>> vfile([True, 'file', 'config.txt']) #файл config.txt не является файлом
    False
    >>> vfile([False, 'file', 'config.txt']) #файл config.txt является файлом
    True
    """
    fname = pathlib.Path(args[2])
    if args[0] == True:
        if fname.is_file():
            return False
        else:
            return True
    else:
        if fname.is_file():
            return True
        else:
            return False


def vhash(args):  # hash
    """
    hash для abs.txt == 546e4328ddf422043a45c460e5f8fe3cd93db06a
    >>> vhash([True, 'hash', '546e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt']) #хэши совпадают
    True
    >>> vhash([True, 'hash', '646e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt']) #хэши не совпадают
    False
    >>> vhash([False, 'hash', '546e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt']) #инверсия для функции работать не должна
    True
    >>> vhash([False, 'hash', '646e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt']) #инверсия для функции работать не должна
    False
    """
    a = hashlib.sha1()
    with open(args[3], "rb") as fh:
        data = fh.read()
        a.update(data)
    if a.hexdigest() == args[2]:
        return True
    else:
        return False


def vuser(args):  # user
    """
    user bono - не существует
    user root - существует
    >>> vuser([True, 'user', 'bono']) #user bono не существует
    True
    >>> vuser([False, 'user', 'bono']) #user bono существует
    False
    >>> vuser([True, 'user', 'root']) #user root не существует
    False
    >>> vuser([False, 'user', 'root']) #user root существует
    True
    """
    if args[0] == True:
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


def vgroup(args):
    """
    >>> vgroup([True, 'group', 'students']) #группы не существует
    True
    >>> vgroup([False, 'group', 'students']) #группа существует
    False
    """
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

doctest.testmod()
