# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую
# их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Каждое слово состоит из латинских букв в нижнем регистре

def my_title(word):
    return word[0].upper()+word[1:]

def isANSi_lower_alpha(word):
    if not word.isascii() or not word.isalpha() or not word.islower():
        return 0
    return 1

def int_func(str):
    word_list = str.split()
    for i, word in enumerate(word_list):
        if isANSi_lower_alpha(word):
            word_list[i] = my_title(word)
        else:
            word_list[i] = 'error_word'

    return ' '.join(word_list)

test_str = 'The quick brown fox jumps over the lazy dog. кот'
print(test_str)
print(int_func(test_str))