# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle


# итератор, генерирующий целые числа, начиная с указанного;
def iter_num(n):
    for i in count(n):
        yield i

# итератор, повторяющий элементы некоторого списка, определённого заранее.
def iter_el(list):
    for el in cycle(list):
        yield el

# выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
for i in iter_num(3):
    if i > 10:
        break
    print(i, end=' ')

print('')
#повторение элементов списка
count = 10
char = 'a' # прикратим цикл если встретим символ 'a' 10 раз
for el in iter_el('qwrasqwe'):
    if count < 0:
        break
    print(el, end=' ')
    if el == char: count -= 1