#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл

chislo = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4_1.txt', 'r') as chislo_start:
    for i in chislo_start:
        i = i.split(' ', 1)
        new_file.append(chislo[i[0]] + '  ' + i[1])

with open('file_4_2.txt', 'w') as chislo_fin:
    chislo_fin.writelines(new_file)
with open('file_4_2.txt') as chislo_fin:
    print(chislo_fin.read())