# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад
# менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

file_name = 'examples5/text_3.txt'
employ_dict = {}

try:
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            line_sp = line.split()
            employ_dict[line_sp[0]] = float(line_sp[1])
except Exception:
    print('Проблемы данными')
else:
    print(f'всего прочитано {len(employ_dict)} строк')
    print('Сотрудники получающие менее 20 000')
    for el in employ_dict.items():
        if float(el[1]) < 20000.0:
            print(' '*5, f'{el[0]}')
    print(f'Средняя ЗП по полному списку: {sum(employ_dict.values())/len(employ_dict):.2f}')