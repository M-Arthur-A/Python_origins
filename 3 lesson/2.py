# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

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


# функция по заданию
def user_contacts(name, surname, year, city, mail, phone):  # лучше бы через *аргс ли кваргс
    atributes = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
    user_atributes = [name, surname, year, city, mail, phone]
    print('Вот, что мы о Вас узнали: ', end=' ')
    for i, text in enumerate(atributes):
        if i == len(atributes)-1:
            print(f'{atributes[i]} - {user_atributes[i]}!')
        else:
            print(f'{atributes[i]} - {user_atributes[i]}, ', end=' ')


name = input_u('Ваше имя?')
surname = input_u('Ваша фамилия?')
year = input_u('Ваш год рождения?')
city = input_u('Ваш город рождения?')
mail = input_u('Ваша почта?')
phone = input_u('Ваш телефон?')
user_contacts(name=name, surname=surname, year=year, city=city, mail=mail, phone=phone)
