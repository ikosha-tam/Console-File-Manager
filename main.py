'''
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
'''


import os
budget = 0

while True:
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

    if choice == '1':       # Создать папку
        print(choice)
        name_dir = input('Имя новой папки: ')
        if not os.path.exists(name_dir):
            os.mkdir(name_dir)
        else:
            print('Папка уже существует!')
    elif choice == '2':     # Удалить (файл/папку)
        print(choice)
        name_dir = input('Имя папки для удаления: ')
        if os.path.exists(name_dir):
            os.rmdir(name_dir)
        else:
            print('Папка для удаления отсутствует!')
    elif choice == '3':     # Копировать (файл/папку)
        print(choice)
    elif choice == '4':     #Просмотр содержимого рабочей директории'
        print(choice)
        print('Текущая папка: ',os.getcwd())
        print(os.listdir())
    elif choice == '5':     # Посмотреть только папки
        print(choice)
    elif choice == '6':     # Посмотреть только файлы
        print(choice)
    elif choice == '7':     # Просмотр информации об операционной системе
        print(choice)
    elif choice == '8':     # Создатель программы
        print(choice)
    elif choice == '9':     # Играть в викторину
        print(choice)
    elif choice == '10':    # Мой банковский счет
        print(choice)
    elif choice == '11':    #Смена рабочей директории (*необязательный пункт)
        print(choice)
    elif choice == '12':    # Выход
        break
    else:
        print('Неверный пункт меню')
