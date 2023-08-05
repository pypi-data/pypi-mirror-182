"""Программа распаковывает *tar.gz архив вложенный как матрешка."""
import tarfile


def req(num, tmp):
    file_name = (tmp % {"number": num})
    print(file_name)
    tar = tarfile.open(file_name)
    tar.extractall('./')
    tar.close()


def zp(templ, count):
    """
    templ str: шаблон вашего архива.

    Example:
        Файл архива: archive-001.tar.gz
        templ = 'archive-%(number)03d.tar.gz'
    """
    for i in range(count):
        req(i + 1, templ)


def bum(templ: str, count: int):
    return zp(templ, count)


if __name__ == '__main__':
    t = 'archive-%(number)03d.tar.gz'
    zp(t, 100)
