'''
Ограничение времени	- 1 секунда
Ограничение памяти	- 64Mb

Задана последовательность целых чисел a1, a2, …, an.
Задаются запросы: сказать любой элемент последовательности на отрезке от L до R включительно,
не равный минимуму на этом отрезке.
'''


n,m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(m):
    L, R = map(int, input().split())
    R+=1
    print(max(arr[L:R]) if min(arr[L:R]) != max(arr[L:R]) else 'NOT FOUND')
