# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
with open("file_7.txt""", "r", encoding="utf-8") as file:
    profit_dict = {}
    av_profit = {}
    looser_av_profit = {}
    my_list = []
    count = 1
    all_profit = 0
    for line in file:
        company = line.split()[0]  # название компании
        income = int(line.split()[2])  # доход
        costs = int(line.split()[3])  # расход
        profit = income - costs  # прибыль
        all_profit += profit  # общая прибыль всех компаний
        if profit > 0:
            profit_dict.update({company: profit})  # словарь компаний с их прибылью
        else:
            looser_av_profit.update({company: profit})  # словарь компаний с их убытками

        count += 1
    average_profit = all_profit / count  # средняя прибыль всех компаний

    av_profit["Average_profit"] = round(average_profit, 3)
    my_list.append(profit_dict)
    my_list.append(av_profit)

with open("file_json_7.json", "w") as write_f:
    json.dump((my_list, looser_av_profit), write_f, indent=4, ensure_ascii=False)