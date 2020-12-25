import pathlib
import doctest
import hashlib
import pwd

def vfile(args):  # file - проверка наличия имени файла
    """
    >>> vfile([True, 'file', 'file']) #файла нет
    True
    >>> vfile([False, 'file', 'file']) #файла нет
    False
    >>> vfile([True, 'file', 'config.txt']) #файл есть
    False
    >>> vfile([False, 'file', 'config.txt']) #файл есть
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
    >>> vhash([True, 'hash', '546e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt'])
    True
    >>> vhash([True, 'hash', '646e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt'])
    False
    >>> vhash([False, 'hash', '546e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt'])
    True
    >>> vhash([False, 'hash', '646e4328ddf422043a45c460e5f8fe3cd93db06a', 'abs.txt'])
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


doctest.testmod()
