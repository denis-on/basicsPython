# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе

def print_type(el):
    if (type(el) == list or type(el) == tuple):
        print(el,' : ',type(el), end=' --> ')
        for e in el:
            print(e, end=' : ')
            print(type(e), end=', ')
    elif(type(el) == dict):
        print(el, ' : ', type(el), end=' --> ')
        for e in el.items():
            print(e[0],' : ',e[1],end=', ')
    else:
        print(el, end=' : ')
        print(type(el), end=', ')


my_list=[12, 3.14, 'python', False, [12,34,56], (1,2,3), {'a':1,'b':2}]

for el in my_list:
    print_type(el)
    print('')

