# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

temp_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(temp_list)

rep = set()
work_list = temp_list.copy()
print( [x for x in temp_list if x not in rep and not work_list.remove(x) and x not in work_list or not not rep.add(x)] )




# позволил себе вариации на тему возможных решений
# т.к. по мне записаное выше сложно в понимании (читабельности)

# вариан решения 1 не эфективный count()
print([n for n in temp_list if temp_list.count(n) == 1])


# вариан решения 2

def my_uni_el(list):
    uni = set()
    rep = set()
    for el in list:
        if el in rep:
            continue
        if el in uni:
            rep.add(el)
            uni.discard(el)
            continue
        uni.add(el)
    return uni

unique = my_uni_el(temp_list) #построим словарь уникальных элементов
print([n for n in temp_list if n in unique])


