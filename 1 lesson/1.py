# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

print('Привет! Давай познакомимся!')
user_name = input('Как тебя зовут?\n- : ')
while True: # проверка на ошибку
    user_age = input('Сколько тебе лет?\n- : ' )
    if user_age.isnumeric() == False:
        print('Требуется ввести число!')
    else:
        break
user_city = input('Откуда ты? (укажи город)\n- : ')

if int(user_age) > 40:
    user_status = ' достопочтенный'
else:
    user_status = ''
print(f'Ну привет,{user_status} {user_name} из города {user_city}!')
