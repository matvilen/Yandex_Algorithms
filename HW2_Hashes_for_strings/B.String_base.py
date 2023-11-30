"""
Ограничение времени	- 1 секунда
Ограничение памяти	- 256Mb

Строка S была записана много раз подряд, после чего от получившейся строки взяли префикс
и дали вам. Ваша задача определить минимально возможную длину исходной строки S.

Формат ввода
В первой и единственной строке входного файла записана строка,
которая содержит только латинские буквы, длина строки не превышает 50000 символов.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
zzz
Вывод
1

Пример 2
Ввод
bcabcab
Вывод
3
"""


st = input()
n = len(st)
x, y = 257, 10
p = 10 ** 9 + 7
res_x, res_y = 0, 0
x_deg, y_deg = [1], [1]
hes_x, hes_y = [0], [0]

#находим хеши полиномов строки
for i, ch in enumerate(st):
    res_x = (res_x * x + ord(ch)) % p
    hes_x.append(res_x)
    x_deg.append((x_deg[i]*x) % p)
    res_y = (res_y * y + ord(ch)) % p
    hes_y.append(res_y)
    y_deg.append((y_deg[i] * y) % p)

#делаем проверку (сравнение) префиксов и суффиксов
for i in range(1, n+1):
    if (hes_x[n-i] + hes_x[i] * x_deg[n-i]) % p == hes_x[n] % p and (hes_y[n-i] + hes_y[i] * y_deg[n-i]) % p == hes_y[n] % p:
            print(i)
            break
if n == 0:
    print(n)
