"""
Ограничение времени	- 15 секунд
Ограничение памяти	- 512Mb

Реализуйте сортировку слиянием, используя алгоритм из предыдущей задачи.

На каждом шаге делите массив на две части, сортируйте их независимо и сливайте
с помощью уже реализованной функции.

Формат ввода
В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 106).
Во второй строке содержатся N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).

Формат вывода
Выведите результат сортировки, то есть N целых чисел, разделенных пробелами, в порядке неубывания.

Пример

Ввод
5
1 5 2 4 3
Вывод
1 2 3 4 5
"""


def merge_sort(ls, n):
    if n > 2:
        n1 = n//2 + (1 if n % 2 != 0 else 0)
        n2 = n//2
        ls1 = merge_sort(ls[:n1], n1)
        ls2 = merge_sort(ls[n1:], n2)
        res_ar = []
        i, j = 0, 0
        num1, num2 = ls1[0], ls2[0]
        while True:
            if num1 <= num2:
                res_ar.append(num1)
                i += 1
                if i < n1:
                    num1 = ls1[i]
                else:
                    break
            else:
                res_ar.append(num2)
                j += 1
                if j < n2:
                    num2 = ls2[j]
                else:
                    break

        return res_ar + (ls1[i::] if i < n1 else ls2[j::])
    else:
        return ls if n <= 1 or ls[0] < ls[1] else ls[::-1]


ar_len = int(input())
arr = list(map(int, input().split())) if ar_len > 0 else []
print(*merge_sort(arr, ar_len))