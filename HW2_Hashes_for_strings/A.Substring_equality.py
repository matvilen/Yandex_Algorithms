"""
Ограничение времени	- 15 секунд
Ограничение памяти	- 512Mb

Дана строка S, состоящая из строчных латинских букв.
Определите, совпадают ли строки одинаковой длины L, начинающиеся с позиций A и B.

Формат ввода
В первой строке записана S (1 ≤ |S| ≤ 2 ⋅ 105), состоящая из строчных латинских букв.
Во второй строке записано число Q (1 ≤ Q ≤ 2 ⋅ 105) — количество запросов.
В следющих Q строках записаны запросы: целые числа
L, A и B (1 ≤ L ≤ |S|, 0 ≤ A, B ≤ (|S| - L)) — длина подстрок и позиции, с которых они начинаются.

Формат вывода
Если строки совпадают — выведите "yes", иначе — "no".

Пример 1
Ввод
acabaca
3
4 3 2
3 4 0
2 0 1

Вывод
no
yes
no
"""


# ввод данных (строки, ее длины и кол-ва запросов)
st = input()
numb_of_req = int(input())
n = len(st)

# переведем строку в числовой формат (полином)
x = 10
y = 1753
p = 10 ** 9 + 13
arr_prefix_x = [0]
arr_prefix_y = [0]
x_deg, y_deg = [1], [1]
res_x, res_y = 0, 0

# зададим префиксы для всех подстрок строки по x и по y
for i, ch in enumerate(st):
    res_x = (res_x * x + ord(ch)) % p
    res_y = (res_y * y + ord(ch)) % p
    arr_prefix_x.append(res_x)
    arr_prefix_y.append(res_y)
    x_deg.append((x*x_deg[i]) % p )
    y_deg.append((y*y_deg[i]) % p )

# сделаем проверку полиномов (подстрок) по всем запросам (если проверка по x прошла, то делаем проверку по y)
for req in range(numb_of_req):
    st_len, from1, from2 = map(int, input().split()) #длина подстрок и позиции, с которых они начинаются
    hx1 = (arr_prefix_x[from1 + st_len] + (arr_prefix_x[from2] * (x_deg[st_len]) if from2 > 0 else 0)) % p
    hx2 = (arr_prefix_x[from2 + st_len] + (arr_prefix_x[from1] * (x_deg[st_len]) if from1 > 0 else 0)) % p
    if hx1 == hx2:
        hy1 = (arr_prefix_y[from1 + st_len] + (arr_prefix_y[from2] * (y_deg[st_len]) if from2 > 0 else 0)) % p
        hy2 = (arr_prefix_y[from2 + st_len] + (arr_prefix_y[from1] * (y_deg[st_len]) if from1 > 0 else 0)) % p
        print('yes' if hy1 == hy2 else 'no')
    else:
        print('no')
