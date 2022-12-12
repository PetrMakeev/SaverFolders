import zipfile
import os

def ZipFiles():
    z = zipfile.ZipFile('d:\\!test\\arc.zip', 'w')        # Создание нового архива
    for root, dirs, files in os.walk('d:\\Backup\\arc'): # Список всех файлов и папок в директории folder
        for file in files:
            z.write(os.path.join(root,file))         # Создание относительных путей и запись файлов в архив

    z.close()