# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Привет! Перемешиваем данные!')
while True:
    # ПРОСИМ ДЛИНУ СПИСКА
    print('Требуется ввести числа для их перемешивания!')
    while True:
        user_count = input('Сколько всего будет значений?\n-> : ')
        if user_count.isnumeric() == False:  # проверка ввода (если ввели не число, а что-то еще)
            print('Вы ввели текст, вместо числа.')
            print('Попробуйте еще!\n')
            continue
        break

    # ПРОСИМ ЗНАЧЕНИЯ ДЛЯ ДОБАВЛЕНИЯ В СПИСОК
    user_list = []
    c = 1
    while c <= int(user_count):
        user_n = input(f'Введите {c} значение\n-> : ')
        user_list.append(user_n)
        c += 1

    # МЕШАЕМ
    check = 1
    for i, l in enumerate(user_list):
        if check <= len(user_list):
            if i == check:
                print(user_list[i])
                user_list[i], user_list[i-1] = user_list[i-1], user_list[i]
                print(user_list[i])
                check += 2

    # ДАЕМ РЕЗУЛЬТАТ
    print('\n---------------------------------------------------------------------------------------------------------')
    print(user_list)
    print('---------------------------------------------------------------------------------------------------------\n')

    # СПРАШИВАЕМ НАДО ЛИ ПОВТОРИТЬ
    repeat = input('Хотите еще перемешать списки? (да / нет)\n-> : ')
    if repeat.lower() == 'нет' or repeat.lower() == 'no':
        break
    else:
        print('\n-----------------------------------------------------------------------------------------------------')
