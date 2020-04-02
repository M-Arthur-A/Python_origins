#     Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
#     возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
#     При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


# вспомогательные функции
def input_u(text, check=False):
    while True:
        user_n = input(f'{text}\n-> : ')
        if check:
            if not user_n.isnumeric():  # проверка ввода (если ввели не число, а что-то еще)
                print('Вы ввели текст, вместо числа.')
                print('Попробуйте еще!\n')
                continue
        break
    if check:
        return int(user_n)
    else:
        return user_n


def print_result(*args):
    print('\n---------------------------------------------------------------------------------------------------------')
    print('РЕЗУЛЬТАТ СЛЕДУЮЩИЙ:')
    print(args if len(args) > 1 else args[0])
    print('---------------------------------------------------------------------------------------------------------\n')


def need_repeat(text):
    """СПРАШИВАЕМ НАДО ЛИ ПОВТОРИТЬ"""
    repeat = input(f'{text} (да / нет)\n-> : ')
    if repeat.lower() == 'нет' or repeat.lower() == 'no' or repeat.lower() == 'n' or repeat.lower() == 'н':
        print('Хорошего дня!')
        return True  # raise RuntimeError('Хорошего дня! До свидания')
    else:
        print('\n-----------------------------------------------------------------------------------------------------')


# функция по заданию
def my_func(x, y, type=0):
    if type == 0:
        return x ** y
    else:
        i = 2
        res = x
        while i <= y:
            res = res * x
            i += 1
        return res


print('Возводим число в степень!')
while True:
    print('Введите число х для возведения его в степень у')
    x = input_u('Введите число x!', True)
    y = abs(int(input_u('Введите степень y!')))
    res = f'Первый вариант: {my_func(x, y)}'
    res2 = f'Второй вариант: {my_func(x, y, 1)}'
    print_result(res, res2)
    if need_repeat('Хотите еще посчитать?'):
        break