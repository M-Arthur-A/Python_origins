# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

print('Привет! Разделим строку на слова!')
while True:
    user_n = input('Введите слова через пробелы\n-> : ')
    print('\n---------------------------------------------------------------------------------------------------------')
    user_list = user_n.split()
    for i, val in enumerate(user_list):
        print(i+1, '|', val[:10])
    print('---------------------------------------------------------------------------------------------------------\n')
