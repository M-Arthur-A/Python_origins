#     Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#     но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


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
def int_func(text, type):
    if type == 1:
        return text.capitalize()
    elif type == 2:
        return text.title()


print('Сделаем правильные буквы заглавными!')
while True:
    user_in = input_u('Введите строку')
    res = int_func(user_in, 1)
    res_ = int_func(user_in, 2)
    print_result(res, res_)
    if need_repeat('Хотите еще?'):
        break
