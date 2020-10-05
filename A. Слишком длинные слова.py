# A. Слишком длинные слова
# https://codeforces.com/contest/71/problem/A

# Иногда некоторые слова вроде «localization» или «internationalization» настолько длинны,
# что их весьма утомительно писать много раз в каком либо тексте.
#
# Будем считать слово слишком длинным, если его длина строго больше 10 символов.
# Все слишком длинные слова можно заменить специальной аббревиатурой.
#
# Эта аббревиатура строится следующим образом: записывается первая и последняя буква слова,
# а между ними — количество букв между первой и последней буквой (в десятичной системе счисления и без ведущих нулей).
#
# Таком образом, «localization» запишется как «l10n», а «internationalization» как «i18n».
#
# Вам предлагается автоматизировать процесс замены слов на аббревиатуры.
# При этом все слишком длинные слова должны быть заменены аббревиатурой, а слова, не являющиеся слишком длинными,
# должны остаться без изменений.
#
# Входные данные
# В первой строке содержится целое число n (1 ≤ n ≤ 100).
# В каждой из последующих n строк содержится по одному слову.
# Все слова состоят из малых латинских букв и имеют длину от 1 до 100 символов.
#
# Выходные данные
# Выведите n строк. В i строке должен находиться результат замены i-го слова из входных данных.
#
# Примеры
# входные данные
# 4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis

# выходные данные
# word
# l10n
# i18n
# p43s



words_count = int(input())
n = words_count
words_list = []
new_words_list = []


while words_count > 0:
     word = input()
     words_list.append(word)
     words_count -= 1

for word in words_list:
     if len(word) > 10:
          x = word[0] + str(len(word)-2) + word[-1]
          new_words_list.append(x)
     else:
          new_words_list.append(word)

for word in new_words_list:
     print(word)