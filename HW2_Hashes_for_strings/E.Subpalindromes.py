"""
Ограничение времени	- 3 секунды
Ограничение памяти	- 256Mb

Строка называется палиндромом, если она читается одинаково как слева направо,
так и справа налево. Например, строки abba, ata являются палиндромами.

Вам дана строка. Ее подстрокой называется некоторая непустая последовательность
подряд идущих символов. Напишите программу, которая определит, сколько подстрок
данной строки является палиндромами.

Формат ввода
Вводится одна строка, состоящая из прописных латинских букв.
Длина строки не превышает 100000 символов.

Формат вывода
Выведите одно число — количество подстрок данной строки, которые являются палиндромами

Пример 1
Ввод
aaa
Вывод
6
Пример 2
Ввод
aba
Вывод
4
"""


#наиболее оптимальное решение

st = input()
n = len(st)
res = 0

# Преобразование строки для учета четности/нечетности длины палиндромов
s = ['#']
for ch in st:
    s.append(ch)
    s.append('#')

p = [0] * len(s)
c, r = 0, 0

for i in range(len(s)):
    mirr = 2 * c - i
    if i < r:
        p[i] = min(r - i, p[mirr])

    # Попытка расширить палиндром
    a, b = i + (1 + p[i]), i - (1 + p[i])
    while a < len(s) and b >= 0 and s[a] == s[b]:
        p[i] += 1
        a += 1
        b -= 1

    # Обновление центра и радиуса текущего палиндрома
    if i + p[i] > r:
        c, r = i, i + p[i]

# Подсчет суммы длин палиндромов
res = sum((length + 1) // 2 for length in p)

print(res)


##сложность N*N
"""
st = input()
n = len(st)
x = 10
p = 10 ** 9 + 7
res_x = 0
x_deg, start_x, end_x = [1], [0], [0]

for i, ch in enumerate(st):
    num = ord(ch)#mdict[ch]
    res_x = (res_x * x + num) % p
    start_x.append(res_x)
    end_x.append((num * x_deg[i] + end_x[i]) % p)
    x_deg.append((x_deg[i] * x) % p)

res = n
for i in range(2, n+1):#длина
    for k in range(i, n+1): #проходка x_deg[k-i+1]
        if (start_x[k] * x_deg[k-i] + end_x[k-i]) % p == (end_x[k] + start_x[k-i] * x_deg[i] * x_deg[k-i]) % p:
            res += 1
print(res)
"""


# Решение с рекурсией (поскольку строка может быть очень длинной,
# а вложенность рекурсий ограничена, то это решение выдает ошибку при больших данных
"""
def check_pal(x1, x2):
    if x1 >= 1 and x2 <= n-2:
        return 1 + check_pal(x1-1, x2+1) if st[x1-1] == st[x2+1] else 0
    else:
        return 0


st = input()
n = len(st)
pal_ar = []
res = n

st_check = st + '!*'
for i, ch in enumerate(st):
    if st_check[i] == st_check[i+1]:
        pal_ar.append((i, i+1))
        res += 1
    if st_check[i] == st_check[i+2]:
        pal_ar.append((i, i+2))
        res += 1

for pair in pal_ar:
    res += check_pal(*pair)

print(res)
"""


# Достаточно оптимальное решение, но немного медленнее, чем самое верхнее
# Нахождение префиксов и суффиксов строки
# Нахождение всех серединок полиномов и нахождение максимальной длины каждого бинарным поиском
"""
st = input()
n = len(st)
res, res_x = n, 0
st += '**'
x, p = 257, 10 ** 9 + 7
x_deg, start_x, end_x, pol_ar_2, pol_ar_3 = [1], [0], [0], [], []

for i, ch in enumerate(st[:-2]):
    num = ord(ch)
    res_x = (res_x * x + num) % p
    start_x.append(res_x)
    if ch == st[i+1]:
        pol_ar_2.append(i)
    if ch == st[i+2]:
        pol_ar_3.append(i)
    end_x.append((num * x_deg[i] + end_x[i]) % p)
    x_deg.append((x_deg[i] * x) % p)


for ind in pol_ar_2:
    ind1 = ind + 1
    n_ind = n - ind1
    len_max = ind1 if ind1 <= n_ind or n_ind < 0 else n_ind
    if (start_x[ind1] * x_deg[ind1] + end_x[ind1]) % p != (end_x[ind1 + len_max] + start_x[ind1 - len_max] * x_deg[len_max] * x_deg[ind1]) % p:
        plus_len, len_min = 1, 1
        minmax = len_max + len_min
        p_len = minmax // 2 + minmax % 2
        while len_min != len_max:
            if (start_x[ind1] * x_deg[ind1] + end_x[ind1]) % p == (end_x[ind1 + p_len] + start_x[ind1 - p_len] * x_deg[p_len] * x_deg[ind1]) % p:
                len_min = p_len
                plus_len = p_len
                minmax = len_max + len_min
                p_len = minmax // 2 + minmax % 2
            else:
                if p_len == len_max:
                    break
                len_max = p_len
                p_len = (len_max + len_min) // 2
    else:
        plus_len = len_max
    res += plus_len


for ind in pol_ar_3:
    len_max = ind+1 if ind+1 <= n - ind - 2 or n - ind - 2 < 0 else n - ind - 2
    if (start_x[ind + 1] * x_deg[ind + 2] + end_x[ind + 2]) % p != (end_x[ind + 2 + len_max] + start_x[ind + 1 - len_max] * x_deg[len_max] * x_deg[ind + 2]) % p:
        plus_len = 1
        len_min = 1
        p_len = (len_max + len_min) // 2 + (len_max + len_min) % 2
        while len_min != len_max and p_len > 1:
            if (start_x[ind+1] * x_deg[ind+2] + end_x[ind+2]) % p == (end_x[ind + 2 + p_len] + start_x[ind + 1 - p_len] * x_deg[p_len] * x_deg[ind+2]) % p:
                plus_len = p_len
                len_min = p_len
                p_len = (len_max + len_min) // 2 + (len_max + len_min) % 2
            else:
                if p_len == len_max:
                    break
                len_max = p_len
                p_len = (len_max + len_min) // 2
        res += plus_len
    else:
        res += len_max

print(res)
"""


#наиболее медленное решение - нахождение серединок полиномов и последующий их подсчет расширением
#при помощи проверки символов строки (не хешей, а именно перебор символов)

"""
st = input()
t0 = time.time()
n = len(st)
res, res_x = n, 0
st += '**'
x, p = 257, 10 ** 9 + 7
x_deg, start_x, end_x, pol_ar_2, pol_ar_3 = [1], [0], [0], [], []

for i, ch in enumerate(st[:-2]):
    if ch == st[i+1]:
        pol_ar_2.append(i)
    if ch == st[i+2]:
        pol_ar_3.append(i)

for ind in pol_ar_2:
    ind1 = ind + 1
    n_ind = n - ind1
    len_max = ind1 if ind1 <= n_ind or n_ind < 0 else n_ind
    if st[ind-len_max+1:ind+len_max] != st[ind-len_max+1:ind+len_max][::-1]:
        plus_len, len_min = 1, 1
        minmax = len_max + len_min
        p_len = minmax // 2 + minmax % 2
        while len_min != len_max:
            if st[ind-p_len+1:ind+len_max] == st[ind-len_max+1:ind+p_len][::-1]:
                len_min = p_len
                plus_len = p_len
                minmax = len_max + len_min
                p_len = minmax // 2 + minmax % 2
            else:
                if p_len == len_max:
                    break
                len_max = p_len
                p_len = (len_max + len_min) // 2
    else:
        plus_len = len_max
    res += plus_len


for ind in pol_ar_3:
    len_max = ind+1 if ind+1 <= n - ind - 2 or n - ind - 2 < 0 else n - ind - 2
    if st[ind - len_max + 1:ind+1 + len_max] != st[ind - len_max + 1:ind + 1 + len_max][::-1]:
        plus_len = 1
        len_min = 1
        p_len = (len_max + len_min) // 2 + (len_max + len_min) % 2
        while len_min != len_max and p_len > 1:
            if st[ind - len_max + 1:ind+1 + p_len] != st[ind - len_max + 1:ind + 1 + p_len][::-1]:
                plus_len = p_len
                len_min = p_len
                p_len = (len_max + len_min) // 2 + (len_max + len_min) % 2
            else:
                if p_len == len_max:
                    break
                len_max = p_len
                p_len = (len_max + len_min) // 2
        res += plus_len
    else:
        res += len_max

print(res)
"""
