# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:                    Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:         30(л)      —     10(лаб)
#                                         Физкультура:      —     30(пр)      —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def raw_line(el):
    """Очищение данных"""
    if ':' in el:
        res = el[:-1]
    elif '—' in el:
        res = 0
    else:
        res = int(el.split('(')[0])
    return res


with open('6_txt.txt') as f:
    lines = f.readlines()
    lessons = {}
    for line in lines:
        line = line.split()
        line = list(map(raw_line, line))
        lessons[line[0]] = sum(line[1:])
    print(f'Результат: {lessons}!')