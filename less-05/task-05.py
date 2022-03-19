# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open("task05.txt", "w+", encoding='utf-8') as f:
    # запишем
    f.write(f"{' '.join(map(str,[randint(1,99) for _ in range(100)]))}")
    # вернемся в начало и прочтем файл
    f.seek(0)
    numbers = [int(i) for i in f.read().split()]
    print(f'Сумма чисел из файла {sum(numbers)}')
