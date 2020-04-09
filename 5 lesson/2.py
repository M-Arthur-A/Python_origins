# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('1_txt.txt') as f:
    lines = f.readlines()
    print(f'Число строк в {f.name} = {len(lines)};')
    for i, line in enumerate(lines):
        print(f'В строке {i + 1} всего {len(line.split())} слов(а).')
