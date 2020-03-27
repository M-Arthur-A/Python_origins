# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('Привет! Это конвертер времени.')
while True:
    print('Для выхода введите: exit или выход')
    user_sec = input('Введите количество секунд\n-> : ')

    # ПРОВЕРКИ
    if (user_sec == 'exit') or (user_sec == 'выход'): # выход из цикла
        break
    if user_sec.isnumeric() == False:  # проверка ввода (если ввели не число, а что-то еще
        print('Вы ввели текст, вместо числа секунд.')
        print('Попробуйте еще!\n')
        continue

    # КОНВЕРТЕР
    if int(user_sec) < 60: # если ввод меньше минуты
        res_hour = '00'
        res_min = '00'
        res_sec = user_sec
    elif int(user_sec) < 60 * 60: # если ввод меньше часа
        res_hour = '00'
        res_min = str(int(user_sec) // 60)
        res_sec = str(int(user_sec) % 60)
    else: # если в вводе есть часы
        res_hour = str(int(user_sec) // (60 * 60))
        user_sec = int(user_sec) % (60 * 60)
        res_min = str(int(user_sec) // 60)
        res_sec = str(int(user_sec) % 60)

    # ФОРМАТИРОВАНИЕ
    # прибавляем 0 в начале, там где 1 число
    res_sec = res_sec if len(res_sec) >= 2 else str(0)+res_sec
    res_min = res_min if len(res_min) >= 2 else str(0)+res_min
    res_hour = res_hour if len(res_hour) >= 2 else str(0)+res_hour
    print('\n---------------------------------------------------------------------------------------------------------')
    print(f'{res_hour}:{res_min}:{res_sec}')
    print('---------------------------------------------------------------------------------------------------------\n')

    # ПОВТОР?
    repeat = input('Хотите еще поконвертировать секунды? (да / нет)\n-> : ')
    if repeat.lower() == 'нет' or repeat.lower() == 'no':
        print(repeat)
        break
    else:
        print('\n-----------------------------------------------------------------------------------------------------')
