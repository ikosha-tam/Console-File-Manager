import random

# соответствие месяца и его названия
months = {
    '01': 'января',
    '02': 'февраля',
    '06': 'июня'
}

# соответствие дня и его названия
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '12': 'двенадцатое',
    '26': 'двадцать шестое'
}

# словарь известных людей и из дат рождения
FAMOUS = {
    'А.С. Пушкин': '26.06.1799',
    'Авраам Линкольн': '12.02.1809',
    'Анджелина Джоли': '04.06.1975'
}


def date_to_str(date):
    """
    Функция приводит дату к текстовому виду
    :param date: дата в формате dd.mm.yyyy
    :return: дата в текстовом виде
    """
    day, month, year = date.split('.')
    result = f'{days[day]} {months[month]} {year} года'
    return result


def run_victory():
    """
    Функция запуска игры викторина
    :return:
    """
    is_play = True
    while is_play:
        # брем 2х из 3х известных людей (только их имена)
        random_famous = random.sample(list(FAMOUS.keys()), 2)
        # идем по именам
        for item in random_famous:
            # просим ввести дату рождения
            answer = input(f'Дата рождения {item} в формате dd.mm.yyyy ')
            # получаем правильный ответ
            true_answer = FAMOUS[item]
            # сравниваем
            if answer == true_answer:
                print('Верно')
            else:
                print('Неверно')
                # получаем дату в текстовом виде
                correct_answer = date_to_str(true_answer)
                # выводим
                print(f'Правильный ответ: {correct_answer}')

        play_again = None
        # Будем спрашивать пока не ответят Да или Нет
        while play_again not in ('Да', 'Нет'):
            play_again = input('Хотите поиграть еще (Да/Нет)? ')

        # Да - продолжаем, Нет - выходим
        is_play = play_again == 'Да'
