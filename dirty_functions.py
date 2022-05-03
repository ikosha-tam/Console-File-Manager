import os
import shutil

def copy_file_or_folder(name, name_new):
    '''
    Функция копирования папки/файла
    :param name: Название папки/файла
    :param name_new: Новое название папки/файла
    :return:
    '''
    if os.path.isfile(name):
        shutil.copy(name, name_new)
    if os.path.isdir(name):
        shutil.copytree(name, name_new)