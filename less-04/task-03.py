#Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

# список генерируемый for
print([n for n in range(20,240,1) if not n % 20 or not n % 21])

# генератор () - распечатываем значения
for i in (n for n in range(20,240,1) if not n % 20 or not n % 21) : print(i, end=" ")