# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
def my_func(list):
    new_list = []
    for i in range(1, len(list), 1):
        if list[i]>list[i-1]: new_list.append(list[i])

    return new_list

temp_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(temp_list)
print(my_func(temp_list))