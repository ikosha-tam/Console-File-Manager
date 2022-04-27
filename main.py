import shutil
import sys
import os
import getpass
import my_module

while True:
    print('-' * 100)
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории (*необязательный пункт)')
    print('12. Выход')
    choice = input('Выберите пункт меню: ')
    if choice == '1':  # Создать папку
        name_dir = input('Имя новой папки: ')
        if not os.path.exists(name_dir):
            os.mkdir(name_dir)
        else:
            print('Папка уже существует!')
    elif choice == '2':  # Удалить (файл/папку)
        name_file_dir = input('Имя файл/папки для удаления: ')
        if os.path.isfile(name_file_dir):
            os.remove(name_file_dir)
            print("Успешно")
        else:
            print("Файл не существует!")
        if os.path.isdir(name_file_dir):
            shutil.rmtree(name_file_dir)
            print("Успешно")
        else:
            print("Папка не существует!")
    elif choice == '3':  # Копировать (файл/папку)
        name = input('Название папки/файла: ')
        name_new = input('Новое название папки/файла: ')
        if os.path.isfile(name):
            shutil.copy(name, name_new)
        if os.path.isdir(name):
            shutil.copytree(name, name_new)
    elif choice == '4':  # Просмотр содержимого рабочей директории'
        print('*** Cодержимого рабочей директории ***')
        list_dir = os.listdir()
        for item in list_dir:
            print(item)
        # print()
    elif choice == '5':  # Посмотреть только папки
        print('*** Папки в директории ***')
        list_dir = os.listdir()
        for item in list_dir:
            if os.path.isdir(item):
                print(item)
    elif choice == '6':  # Посмотреть только файлы
        print('*** Файлы в директории ***')
        list_dir = os.listdir()
        for item in list_dir:
            if os.path.isfile(item):
                print(item)
    elif choice == '7':  # Просмотр информации об операционной системе
        print(sys.platform)
    elif choice == '8':  # Создатель программы
        print('Dmitry I')
    elif choice == '9':  # Играть в викторину
        my_module.victory()
    elif choice == '10':  # Мой банковский счет
        my_module.my_bank_account()
    elif choice == '11':  # Смена рабочей директории (*необязательный пункт)
        print("Текущая директория:", os.getcwd())
        p = os.path.normpath(os.path.join("/home",getpass.getuser()))
        os.chdir(p)
        print("Переход в домашнюю папку в Linux):", os.getcwd())
    elif choice == '12':  # Выход
        break
    else:
        print('Неверный пункт меню')
