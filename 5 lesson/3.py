# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


def average(lst):
    lst = list(map(float, lst))
    return sum(lst) / len(lst)


if __name__ == '__main__':
    with open('3_txt.txt') as f:
        db = {}
        for line in f.readlines():
            data = line.split()
            db[data[0]] = data[1]
        workers_20k = []
        for name, income in db.items():
            if float(income) <= 20000.00:
                workers_20k.append(name)
        workers_20k = ', '.join(workers_20k)
        print(f'Заработная плата менее 20 тысяч установлена следующим сотрудникам: {workers_20k}.')
        print(f'Среднеарифметическая заработная плата в компании составляет {average(list(db.values()))}.')
