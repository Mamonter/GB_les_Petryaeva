# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя


param = {'название': '', 'цена': '', 'кол-во': '', 'ед': ''}
analys = {'название': [], 'цена': [], 'кол-во': [], 'ед': []}
tovar = []
num = 0
param2 = None
control = None
while True:
    control = input("Чтобы продолжить 'Enter', для вывода анализа нажмите латинскую'A' >>").upper()
    num += 1
    if control == 'A':
        print(f'Выводим на экран')
        for category, value in analys.items():
            print(f'{category}: {value}')
    for f in param.keys():
        param2 = input(f'введите "{f}" >>')
        param[f] = int(param2) if (f == 'latin') else param2
        analys[f].append(param[f])
    tovar.append((num, param))

