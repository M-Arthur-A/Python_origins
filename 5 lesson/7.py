# Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import importlib
my_module = importlib.import_module('3')  # модули с числовым именем просто import'ом не импортируются
import json

with open('7_txt.txt') as f:
    profits = {}
    for line in f.readlines():
        line = line.split()
        profits[line[0]] = int(line[2]) - int(line[3])

avg_profit = [i for i in list(profits.values()) if i > 0]
avg_profit = my_module.average(avg_profit)  # берем функцию из 3 задания

to_json = [profits, {'average_profit': avg_profit}]

with open('7_txt.json', 'w') as f:
    json.dump(to_json, f)

print(f'{json.dumps(to_json)} сохранено в {f.name}!')
