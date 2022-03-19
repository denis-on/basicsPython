# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json


file_name = "examples5/text_7.txt"
dig_firm = {}
num_firm = 0
aver_profit = 0
with open(file_name, "r", encoding='utf-8') as fr:
        for line in fr:
            name, type_own, rev, cost = line.split()
            profit = int(rev)-int(cost)
            if profit >= 0:
                aver_profit += profit
                num_firm += 1
            dig_firm[name] = profit
aver_profit /= num_firm

with open('examples5/task07.json', "w", encoding='utf-8') as f:
    json.dump([dig_firm, {"average_profit": aver_profit}], f, ensure_ascii=False)

