# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

translator = {'One': 'Один',
              'Two': 'Два',
              'Three': 'Три',
              'Four': 'Четыре'}

with open('4_txt.txt') as f_old:
    with open('4_txt_res.txt', 'w') as f_new:
        for line in f_old.readlines():
            line_old = line.split()
            line_new =  f'{translator[line_old[0]]} {line_old[1]} {line_old[2]}\n'
            f_new.write(line_new)
