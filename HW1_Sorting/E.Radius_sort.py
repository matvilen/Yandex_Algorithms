"""
Ограничение времени	- 1 секунда
Ограничение памяти	- 64Mb

Поразрядная сортировка является одним из видов сортировки, которые работают
практически за линейное от размера сортируемого массива время. Такая скорость
достигается за счет того, что эта сортировка использует внутреннюю структуру
сортируемых объектов. Изначально этот алгоритм использовался для сортировки
перфокарт. Первая его компьютерная реализация была создана в университете MIT
Гарольдом Сьюардом (Harold Н. Seward). Опишем алгоритм подробнее. Пусть задан
массив строк s1 , ..., si причём все строки имеют одинаковую длину m. Работа а
лгоритма состоит из m фаз. На i -ой фазе строки сортируются па i -ой с конца букве.
Происходит это следующим образом. Будем, для простоты, в этой задаче рассматривать
строки из цифр от 0 до 9. Для каждой цифры создается «корзина» («bucket»), после
чего строки si распределяются по «корзинам» в соответствии с i-ой цифрой с конца.
Строки, у которых i-ая с конца цифра равна j попадают в j-ую корзину (например,
строка 123 на первой фазе попадет в третью корзину, на второй — во вторую,
на третьей — в первую). После этого элементы извлекаются из корзин в порядке
увеличения номера корзины. Таким образом, после первой фазы строки отсортированы по
последней цифре, после двух фаз — по двум последним, ..., после m фаз — по всем.
При важно, чтобы элементы в корзинах сохраняли тот же порядок, что и в исходном
массиве (до начала этой фазы). Например, если массив до первой фазы имеет вид:
111, 112, 211, 311, то элементы по корзинам распределятся следующим образом:
в первой корзине будет. 111, 211, 311, а второй: 112. Напишите программу,
детально показывающую работу этого алгоритма на заданном массиве.

Формат ввода
Первая строка входного файла содержит целое число n (1 ≤ n ≤ 1000) .
Последующие n строк содержат каждая по одной строке si .
Длины всех si , одинаковы и не превосходят 20. Все si состоят только из цифр от 0 до 9.

Формат вывода
В выходной файл выведите исходный массив строк в, состояние «корзин» после распределения
элементов по ним для каждой фазы и отсортированный массив. Следуйте формату, приведенному в примере.

Пример
Ввод	Вывод
9
12
32
45
67
98
29
61
35
09
Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98
"""


n = int(input())    # длина массива
ls = []
k_phases = 0    # кол-во разрядов в наибольшем числе

# вводим массив в виде строк и иещем наибольшее кол-во разрядов
for i in range(n):
    num = input()
    ls.append(num.zfill(k_phases))
    len_num = len(num)
    if len_num > k_phases:
        k_phases = len_num

# переписываем строки-числа массива с учетом незначащих нулей
for num in ls:
    num.zfill(k_phases)

# Делаем красивый вывод в соответствии с заданием
print("Initial array:")
print(*ls, sep=', ')
print('**********')

# Инициализируем два словаря (1ый - заполним единицами, а потом из 1ого
# будем наполнять 2ой, когда 2ой наполним, то сделаем так чтобы 1ый
# ссылался на 2ой, а 2ой снова сделаем пустым, чтобы потом снова заполнить его из 1ого
buckets_start = {str(i): [] for i in range(10)}
buckets_end = {str(i): [] for i in range(10)}

# Раскидаем числа массива по корзинкам 1ого словаря
for num in ls:
    buckets_start[num[-1]].append(num)

for phase in range(1, k_phases):
    print('Phase', phase)
    for key, bucket in buckets_start.items():
        for num in bucket:
            # заполняем 2ой словарь строками из массива каждой корзины 1ого словаря
            buckets_end[num[-phase-1]].append(num)
        #делаем вывод корзин, ИЗ КОТОРЫХ заполнили следующие (а не тех, что только что заполнили)
        print("Bucket", key+':', end = ' ')
        print(*bucket, sep=', ') if len(bucket) > 0 else print("empty")
    print('**********')
    # обнуляем словари (см. коммент при инициализации)
    buckets_start = buckets_end
    buckets_end = {str(i): [] for i in range(10)}

ls = []
print('Phase', k_phases)
# вывод последних заполненных корзин + формирование отсортированного массива
for key, bucket in buckets_start.items():
    print("Bucket", key+':', end = ' ')
    print(*bucket, sep=', ') if len(bucket) > 0 else print("empty")
    ls = ls + bucket

print('**********', 'Sorted array:', sep='\n')
print(*ls, sep=', ')