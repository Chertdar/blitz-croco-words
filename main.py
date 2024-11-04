import os
from zipfile import ZipFile

current_file = os.path.relpath(__file__)
current_directory = os.path.dirname(current_file)

PATH_FILE_ZIP = "croco-blitz-source.zip"


def zip_f():
    with ZipFile(PATH_FILE_ZIP, mode="r") as archive:
        print("Список файлов в архиве: ")
        for f in archive.namelist():
            print(f)


if __name__ == '__main__':
    print(current_file)

    zip_f()
