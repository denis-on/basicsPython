# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

def inputIntNum(message):
    n=-1
    while True:
        try:
            n = int(input(message + ' '))
        except ValueError:
            print('Это не число, попробуйте снова.')
        else:
            if n < 0:
                print('Введено отрицательное значение!')
                continue
            break
    return n


my_list = [7, 5, 3, 3, 2]
print(my_list)
number = inputIntNum('Введите натуральное число или "0" для выхода:')

while number >0:
    c=len(my_list)
    if number not in my_list: # если нет элемента то найдем куда вставить
        for i in range(c):
            if number > my_list[i]:
                my_list.insert(i,number)
                break
            if i == c-1:
                my_list.append(number)
    else:
        indx = my_list.count(number)
        my_list.insert(indx, number)

    print(my_list)
    number = inputIntNum('Введите натуральное число или "0" для выхода')
