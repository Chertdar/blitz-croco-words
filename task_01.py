# подключение библиотек
import os
from pathlib import Path
from zipfile import ZipFile

# константа имени файла
ZIP_FILENAME = "croco-blitz-source.zip"


# функция read_zipped_file не принимающая на вход нечего для чтения zip-файла
def read_zipped_file():
    # чтение текущей директирией
    current_folder = os.path.dirname(os.path.realpath(__file__))

    # открытие файла в текущей директорией
    with ZipFile(Path(current_folder) / 'src' / ZIP_FILENAME) as archive:
        for f in archive.namelist():
            print(f)  # вывод на экран всех файлов


if __name__ == "__main__":
    read_zipped_file()
