import random
import os
import json

def victory():
    birthdays_dict = {
        'Юрий Алексеевич Гагарин': '09.03.1934',
        'Александр Сергеевич Пушкин': '06.06.1799',
        'Владимир Ильич Ленин': '22.04.1870',
        'Сергей Павлович Королёв': '12.01.1907',
        'Владимир Вольфович Жириновский': '25.04.1946',
        'Михаил Васильевич Ломоносов': '19.11.1711',
        'Игорь Васильевич Курчатов': '12.01.1903',
        'Дмитрий Иванович Менделеев': '08.02.1834',
        'Альберт Эйнштейн': '14.03.1879',
        'Роджер Уотерс': '06.09.1943'
    }
    days = {
        '01': 'первое',
        '02': 'второе',
        '03': 'третье',
        '04': 'четвертое',
        '05': 'пятое',
        '06': 'шестое',
        '07': 'седьмое',
        '08': 'восьмое',
        '09': 'девятое',
        '10': 'десятое',
        '11': 'одиннадцатое',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шестнадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'двадцатое',
        '21': 'двадцать первое',
        '22': 'двадцать второе',
        '23': 'двадцать третье',
        '24': 'двадцать четвертое',
        '25': 'двадцать пятое',
        '26': 'двадцать шестое',
        '27': 'двадцать седьмое',
        '28': 'двадцать восьмое',
        '29': 'двадцать девятое',
        '30': 'тридцатое',
        '31': 'тридцать первое'
    }
    months = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря',
    }
    name_list = list(birthdays_dict.keys())
    random_name_list = random.sample(name_list, 5)
    print('Вводите дату в формате (dd.mm.yyyy)')
    number_correct_answers = 0
    number_incorrect_answers = 0
    repit_quiz = 'Y'
    while repit_quiz == 'Y':
        for quest in random_name_list:
            data = input(f'{quest}:')
            if data == birthdays_dict[quest]:
                print('    ВЕРНО!')
                number_correct_answers += 1
            else:
                data = birthdays_dict[quest]
                day, month, year = data.split('.')
                print('    НЕВЕРНО! Правильный ответ:', days[day], months[month], year, 'года')
                number_incorrect_answers += 1
        print('-' * 60)
        print('количество правильных ответов -', number_correct_answers)
        print('количество неверных ответов -', number_incorrect_answers)
        number_correct_answers = 0
        number_incorrect_answers = 0
        repit_quiz = input('начать снова - Y, выход - ENTER:')
    print('До встречи!!!')


def my_bank_account():
    FILE_BUDGET = 'budget.data'
    FILE_HISTORY = 'history_purchase.json'
    budget = 0
    history = []

    def print_history():
        for item, cost in history:
            print(f'{item}:\t {cost} руб.')

    if os.path.exists(FILE_BUDGET):
        with open(FILE_BUDGET, 'r') as f:
            budget = int(f.read())

    if os.path.exists(FILE_HISTORY):
        with open(FILE_HISTORY, 'r') as h:
            history = json.load(h)
            print('Ваши предыдущие покупки:')
            print_history()

    def purchase(budget):
        sum = int(input('Введите стоимость покупки: '))
        if sum > budget:
            print('Недостаточно средств')
        else:
            budget -= sum
            name = input('Введите название покупки: ')
            history.append((name, sum))
        return budget

    while True:
        print(f'Ваш счет: {budget}')
        print('-' * 100)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню: ')
        print('-' * 100)
        if choice == '1':
            sum = int(input('Введите сумму для пополнения: '))
            budget += sum
        elif choice == '2':
            budget = purchase(budget)
        elif choice == '3':
            print('История покупок:')
            print_history()
        elif choice == '4':
            with open(FILE_BUDGET, 'w') as f:
                f.write(str(budget))
            with open(FILE_HISTORY, 'w') as h:
                json.dump(history, h)
            break
        else:
            print('Неверный пункт меню')


def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count


def date_to_str(date):
    """
    Функция приводит дату к текстовому виду
    :param date: дата в формате dd.mm.yyyy
    :return: дата в текстовом виде
    """
    day, month, year = date.split('.')
    result = f'{days[day]} {months[month]} {year} года'
    return result
