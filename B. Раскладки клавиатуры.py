# B. Раскладки клавиатуры
# https://codeforces.com/problemset/problem/831/B

# В Берляндии распространены две раскладки для клавиатур, которые различаются только порядком следования букв на клавишах.
# Все остальные клавиши совпадают. В Берляндии используют алфавит, который содержит 26 букв и совпадает с английским.
#
# Вам будут заданы две строки по 26 букв в каждой — все клавиши первой и второй раскладки в порядке слева направо сверху вниз.
#
# Также вам будет задан набранный текст, который состоит из прописных и строчных букв английского алфавита и цифр.
# Известно, что он был набран по ошибке в первой раскладке, хотя хотели набрать его во второй. Выведите этот текст,
# если бы использовалась вторая раскладка, а не первая при его наборе.
#
# Так как все клавиши кроме буквенных совпадают, то регистр букв и символы отличные от букв остаются неизменными.
#
# Входные данные
# В первой строке следует строка длины 26, состоящая из различных строчных букв латинского алфавита — первая раскладка.
#
# Во второй строке следует строка длины 26, состоящая из различных строчных букв латинского алфавита — вторая раскладка.
#
# В третьей строке следует непустая строка s, состоящая из строчных и заглавных латинских букв, а также цифр — набранный
# текст в первой раскладке. Длина строки s не превосходит 1000.
#
# Выходные данные
# Выведите текст, если бы он был набран во второй раскладке.
#
# Примеры
# входные данные
# qwertyuiopasdfghjklzxcvbnm
# veamhjsgqocnrbfxdtwkylupzi
# TwccpQZAvb2017
# выходные данные
# HelloVKCup2017
# входные данные
# mnbvcxzlkjhgfdsapoiuytrewq
# asdfghjklqwertyuiopzxcvbnm
# 7abaCABAABAcaba7
# выходные данные
# 7uduGUDUUDUgudu7


keyboard_1 = list(input())
keyboard_2 = list(input())

text = list(input())
new_text = ''

for i in range(len(text)):
    if text[i].islower():
        index = keyboard_1.index(text[i])
        new_text += keyboard_2[index]
    elif text[i].isupper():
        index = keyboard_1.index(text[i].lower())
        new_text += keyboard_2[index].upper()
    else:
        new_text += text[i]


print(new_text)

