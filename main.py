# Теперь рефакторим код.
# Ракладываем его по уровням и задачам.
# 1 уровень - читаем архив и собираем слова из каждого файла
# 2 уровень (ниже) - читаем файл с презентацией и достаём из него слова.
# Уровни лучше разнести по разным файлам.


import os
from zipfile import ZipFile
from pathlib import Path
from helpers import get_words_presentation, write_txt

FILE_ZIP = 'src/croco-blitz-source.zip'


def unzip_zip_file():
    cur_folder = os.path.dirname(os.path.realpath(__file__))
    words: set[str] = set()

    p = Path(cur_folder) / FILE_ZIP

    with ZipFile(p) as zip_ref:
        for f in zip_ref.namelist():
            words.update(get_words_presentation(zip_ref.open(f)))

    write_txt("words.txt", words)


if __name__ == '__main__':
    unzip_zip_file()


