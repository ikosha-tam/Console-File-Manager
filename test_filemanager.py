'''
4. В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
Если в проекте нет функций либо не получается написать ни одного теста, можно использовать мою урезанную версию
данного проекта по ссылке: https://yadi.sk/d/n6gyaovRG2JdAA
'''

from filemanager import author_info
import my_module, victory

# тесты для каждой ""чистой"" функции
def test_author_info():
    assert author_info() == 'Leonid Orlov'

def test_separator():
    str_separator = '*' * 30
    assert my_module.separator(count=30) == str_separator

def test_date_to_str():
    assert victory.date_to_str('04.06.1975') == 'четвертое июня 1975 года'

