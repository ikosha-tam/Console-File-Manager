'''
тесты для ""грязных"" функций
'''

import os
from dirty_functions import copy_file_or_folder


# копирования файла/папки
def test_copy_file_or_folder():
    # копирование файла
    if not os.path.exists('test_file.txt'):
        my_file = open('test_file.txt', 'w+')
        my_file.close()
    if os.path.exists('test_file_copy.txt'):
        os.remove('test_file_copy.txt')
    copy_file_or_folder('test_file.txt', 'test_file_copy.txt')
    assert os.path.exists('test_file_copy.txt')

    # копирование папки
    if not 'TEST_DIR' in os.listdir():
        os.mkdir('TEST_DIR')
    if 'TEST_DIR_COPY' in os.listdir():
        os.rmdir('TEST_DIR_COPY')
    copy_file_or_folder('TEST_DIR', 'TEST_DIR_COPY')
    assert 'TEST_DIR_COPY' in os.listdir()