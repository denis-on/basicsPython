# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#
while True:
    try:
        num = int(input('Введите целое положительное число: '))
    except ValueError:
        print('Это не число, попробуйте снова.')
    else:
        if num < 0:
            print('неверно')
            continue
        break

num_stat = num
single = 0
while num > 0:
    rem = num % 10
    print(rem, end=" ")
    single = rem if rem > single else single
    num = num // 10
print('')
print('%d наибольшая цифра в числе %d' % (single, num_stat) )

