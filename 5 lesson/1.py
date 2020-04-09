# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import my_funcslib as mfl

with open('1_txt.txt', 'w') as f:
    while True:
        user_input = mfl.input_u('Введите строку.')
        if user_input == '':
            break
        f.write(user_input + '\n')
