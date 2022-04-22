"""
history = []

def purchase(budget):
    sum = int(input('Введите стоимость покупки: '))
    if sum > budget:
        print('Недостаточно средств')
    else:
        budget -= sum
        name = input('Введите название покупки: ')
        history.append((name, sum))
    return budget


    print(f'Ваш счет: {budget}')


    sum = int(input('Введите сумму для пополнения: '))
    budget += sum

    sum = int(input('Введите сумму для пополнения: '))
    budget += sum

    budget = purchase(budget)

    for item, cost in history:
        print(f'{item}:\t {cost} руб.')
    print(history)

    print('Текущая папка: ', os.getcwd())
    print(os.listdir())
"""
import shutil
import sys
import os
import getpass

budget = 0

while True:
    print('-' * 100)
    print('1. Создать папку')  # Сделано
    print('2. Удалить (файл/папку)')  # Сделано
    print('3. Копировать (файл/папку)')  # Сделано
    print('4. Просмотр содержимого рабочей директории')  # Сделано
    print('5. Посмотреть только папки')  # Сделано
    print('6. Посмотреть только файлы')  # Сделано
    print('7. Просмотр информации об операционной системе')  # Сделано
    print('8. Создатель программы')  # Сделано
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
        print(getpass.getuser())
    elif choice == '9':  # Играть в викторину
        print(choice)
    elif choice == '10':  # Мой банковский счет
        print(choice)
    elif choice == '11':  # Смена рабочей директории (*необязательный пункт)
        print(choice)
    elif choice == '12':  # Выход
        break
    else:
        print('Неверный пункт меню')
