
# A. I Wanna Be the Guy
# http://codeforces.com/problemset/problem/469/A?locale=ru

# Есть такая игра под названием «I Wanna Be the Guy», в ней n уровней. Little X и его друг Little Y подсели на эту игру.
# Каждый из них хочет пройти игру полностью.
#
# Little X может пройти только p уровней этой игры. А Little Y может пройти только q уровней этой игры.
# Вам даны номера уровней, которые может пройти Little X, и номера уровней, которые может пройти Little Y.
# Могут ли Little X и Little Y пройти игру полностью, если объединят свои усилия?
#
# Входные данные
# В первой строке записано единственное целое число n (1 ≤  n ≤ 100).
#
# В следующей строке сначала записано целое число p (0 ≤ p ≤ n), затем следуют p различных целых чисел a1, a2, ..., ap (1 ≤ ai ≤ n).
# Эти числа обозначают номера уровней, которые может пройти Little X. В следующей строке содержатся номера уровней, которые может пройти Little Y, в аналогичном формате.
# Предполагается, что уровни пронумерованы от 1 до n.
#
# Выходные данные
# Если друзья могут пройти все уровни вместе, выведите «I become the guy.». Если это невозможно, выведите «Oh, my keyboard!» (без кавычек).
#
# Примеры
# входные данные
# 4
# 3 1 2 3
# 2 2 4
# выходные данные
# I become the guy.
# входные данные
# 4
# 3 1 2 3
# 2 2 3
# выходные данные
# Oh, my keyboard!


n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a1 = set(a[1::])
b1 = set(b[1::])

c = a1 | b1

if len(c) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

