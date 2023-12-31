"""
Ограничение времени	- 1 секунда
Ограничение памяти	- 64Mb

Чтобы оценить качество обучения программированию, в каждой группы студентов
подсчитывается один параметр — суммарное количество решенных студентами задач.

Известно, что в первой группе суммарное количество решенных на контесте задач
равно a, а во второй — b. Всего на контесте было предложено n задач, а также известно,
что каждый студент решил не менее одной (и не более n) задач.

По заданным a, b и n определите, могло ли в первой группе быть строго больше студентов,
чем во второй.

Формат ввода
Вводятся три целых числа a, b, n (0 ≤ a, b ≤ 10000, 1 ≤ n ≤ 10000).

Формат вывода
Выведите "Yes" если в первой группе могло быть строго больше студентов,
чем во второй, и "No" в противном случае.

Пример 1
Ввод
60
30
4
Вывод
Yes

Пример 2
Ввод
30
30
1
Вывод
No
Пример 3
Ввод
30
150
4
Вывод
No
"""

a, b, n = int(input()), int(input()), int(input())
if a > b:
    print('Yes')
elif a == b:
    print('Yes') if n > 1 else print('No')
else:
    print('Yes') if b // n + (1 if b % n > 0 else 0) < a else print('No')
