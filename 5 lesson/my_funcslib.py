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


if __name__ == '__main__':
    pass
