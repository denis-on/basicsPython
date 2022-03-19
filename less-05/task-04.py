# Создать (не программно) текстовый файл со следующим содержимым:
#
#One — 1
#Two — 2
#Three — 3
#Four — 4
#
#Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.


file_name = 'examples5/text_4.txt'
dig = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре', 'Five':'Пять',
       'Six':'Шесть', 'Seven':'Семь', 'Eight':'Восемь', 'Nine':'Девять',}

with open(file_name, "r", encoding='utf-8') as fr, open("task04.txt", "w", encoding='utf-8') as fw:
        for line in fr:
            eng, sep, num = line.split()
            # print(f'{dig[eng]} {sep} {num}')
            print(f'{dig[eng]} {sep} {num}', file=fw)

