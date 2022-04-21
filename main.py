
budget = 0
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

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет: {budget}')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        sum = int(input('Введите сумму для пополнения: '))
        budget += sum
    elif choice == '2':
        budget = purchase(budget)
    elif choice == '3':
        for item, cost in history:
            print(f'{item}:\t {cost} руб.')
        # print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
