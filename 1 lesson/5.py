# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток —
# издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

while True:
    print('Привет! Это Ваш личный финансовый помощник.')
    print('Для выхода введите: exit или выход')

    while True:
        revenue = input('Введите выручку компании\n-> : ')
        if (revenue == 'exit') or (revenue == 'выход'): # выход из 1 цикла
            break
        if revenue.isnumeric() == False:  # проверка ввода (если ввели не число, а что-то еще)
            print('Вы ввели не число.')
            print('Попробуйте еще!\n')
            continue
        break
    if (revenue == 'exit') or (revenue == 'выход'):  # выход из 2 цикла (программы)
        break
    while True:
        costs = input('Введите издержки компании\n-> : ')
        if (costs == 'exit') or (costs == 'выход'): # выход из 1 цикла
            break
        if costs.isnumeric() == False:  # проверка ввода (если ввели не число, а что-то еще)
            print('Вы ввели не число.')
            print('Попробуйте еще!\n')
            continue
        break
    if (costs == 'exit') or (costs == 'выход'): # выход из 2 цикла (программы)
        break
    income = int(revenue) >= int(costs)
    if income:
        print(f'Ух ты! Да эта компания работает в прибыль ({int(revenue) - int(costs)})')
        print(f'А ее рентабельность выручки составляет {(int(revenue) - int(costs)) / int(revenue)*100}%')
        while True:
            workers = input('\nА теперь давайте узнаем сколько человек работает в этой компании\n-> : ')
            if (workers == 'exit') or (workers == 'выход'):  # выход из 1 цикла
                break
            if workers.isnumeric() == False:  # проверка ввода (если ввели не число, а что-то еще)
                print('Вы ввели не число.')
                print('Попробуйте еще!\n')
                continue
            break
        if (workers == 'exit') or (workers == 'выход'):  # выход из 2 цикла (программы)
            break
        print(f'Прибыль фирмы в расчете на одного сотрудника составляет {(int(revenue) - int(costs)) / int(workers):.1f}')

    else:
        print(f'К сожалению, эта компания работает в убыток {int(revenue) - int(costs)}')
    repeat = input('Хотите просчитать другую компанию? (да / нет)\n-> : ')
    if repeat.lower() == 'нет' or repeat.lower() == 'no':
        print(repeat)
        break
    else:
        print('\n-----------------------------------------------------------------------------------------------------')
