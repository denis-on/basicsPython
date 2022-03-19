# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


file_name = 'examples5/text_7.txt'
lines = 0
words = 0

try:
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            words_in_line = len(line.split())
            lines += 1
            words += words_in_line
            print(f'строка {lines} содержит {words_in_line} слов')
except Exception:
    print('Проблемы данными')
else:
    print(f'Из файла прочитано {lines} строка и всего {words} слов')


