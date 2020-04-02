# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


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
    """СПРАШИВАЕМ НАДО ЛИ ПОВТОРИТЬ. Функция возвращает bool"""
    repeat = input(f'{text} (да / нет)\n-> : ')
    if repeat.lower() == 'нет' or repeat.lower() == 'no' or repeat.lower() == 'n' or repeat.lower() == 'н':
        print('Хорошего дня!')
        return True  # raise RuntimeError('Хорошего дня! До свидания')
    else:
        print('\n-----------------------------------------------------------------------------------------------------')


# функция по заданию
def user_divide(x, y):
    try:
        res = int(x) / int(y)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        res = 'Н/Д'
    return res


while True:
    user_n_one = input_u('Введите делимое.', True)
    user_n_two = input_u('Введите делитель.', True)
    res = user_divide(user_n_one, user_n_two)
    if res == 'Н/Д':
        continue
    else:
        print_result(res)
        if need_repeat('Продолжим?'):
            break
