import math

# Тесты для встроенных функций filter, map, sorted
def test_filter():
    mixed = ['мак', 'рис', 'мак', 'мак', 'просо', 'мак', 'пшено', 'горох', 'ячмень', 'мак']
    assert list(filter(lambda x: x == 'мак', mixed)) == ['мак', 'мак', 'мак', 'мак', 'мак']
    numbers_tuple = (-2, -1, 0, 1, 2, 3, 4, 5)
    assert tuple(filter(lambda x: x >= 0, numbers_tuple)) == (0, 1, 2, 3, 4, 5)
    assert tuple(filter(lambda x: x < 0, numbers_tuple)) == (-2, -1)


# Тесты для функций из библиотеки math: pi, sqrt, pow, hypot
def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt():
    assert math.sqrt(144) == 12
    assert math.sqrt(256) == 16
    assert math.sqrt(1024) == 32
    assert math.sqrt(99) == 9.9498743710662

def test_pow():
    assert math.pow(3, 2) == 9
    assert math.pow(10, 3) == 1000
    assert math.pow(10, -3) == 0.001
    assert math.pow(3, 3.5) == 46.76537180435969

def test_hypot():
    assert math.hypot(4, 1) == 4.123105625617661
    assert math.hypot(-2, 0) == 2
    assert math.hypot(-1, 2) == 2.23606797749979



