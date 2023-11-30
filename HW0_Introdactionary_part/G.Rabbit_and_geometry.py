"""
Ограничение времени	- 4 секунда
Ограничение памяти	- 80Mb

Кролики очень любопытны. Они любят изучать геометрию, бегая по грядкам.
Наш кролик как раз такой. Сегодня он решил изучить новую фигуру — квадрат.
Кролик бегает по грядке — клеточному полю N × M клеток.
В некоторых из них посеяны морковки, в некоторых нет.
Помогите кролику найти сторону квадрата наибольшей площади,
заполненного морковками полностью.

Формат ввода
В первой строке даны два натуральных числа N и M (1<=N, M<=1000).
Далее в N строках расположено по M чисел, разделенных пробелами
(число равно 0, если в клетке нет морковки или 1, если есть).

Формат вывода
Выведите одно число — сторону наибольшего квадрата, заполненного морковками.

Пример 1
Ввод
4 5
0 0 0 1 0
0 1 1 1 0
0 0 1 1 0
1 0 1 0 0
Вывод
2

Пример 2
Ввод
10 10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
Вывод
10

Пример 3
Ввод
10 10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
Вывод
0
"""

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Создаем матрицу dp для хранения длин сторон максимальных квадратов
dp = [[0] * M for _ in range(N)]
max_side = 0 #макс сторона квадрата

for i in range(N):
    for j in range(M):
        # Если текущий элемент равен 1, то
        if grid[i][j] == 1:
            # Устанавливаем длину стороны квадрата в 1
            dp[i][j] = 1
            # Если не находимся на верхней или левой границе матрицы,
            # обновляем длину стороны квадрата, исходя из значений выше, слева и по диагонали выше-слева
            if i > 0 and j > 0:
                dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            max_side = max(max_side, dp[i][j])

print(max_side)

#наглядное пояснение к алгоритму
#https://www.youtube.com/watch?v=aYnEO53H4lw


#первоначальное менее оптимальное решение
"""
def check_round_sqvr(st_i, st_j, matrx, l):
    if st_i >= n or st_j >= m:
        key = False
    else:
        key = True
        for i in range(l):
            if matrx[st_i-i][st_j] == 0 or matrx[st_i][st_j-i] == 0:
                key = False
                break
    return check_round_sqvr(st_i+1, st_j+1, matrx, l+1) if key else (l-1, st_i, st_j)    # and st_i+1 < n and st_j+1 < m


def check_matrix(n1, n2, m1, m2, check_h):

    if check_h > n2 - n1 or check_h > m2 - m1:
        return 0

    mhand, hand, hand1, hand2, hand3, hand4 = 0, (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)
    sq1, sq2, sq3, sq4 = False, False, False, False

    for i in range(n1, n2, 2):
        for j in range(m1, m2, 2):
            if rabb_ter[i][j] == 1:
                #if (i, j) in pass_set:

                if rabb_ter[i-1][j] == 1:
                    if rabb_ter[i-1][j-1] == rabb_ter[i][j-1] == 1:
                        sq1 = True
                    if j+1 < m and rabb_ter[i-1][j+1] == rabb_ter[i][j+1] == 1 :
                        sq2 = True
                if i+1 < n and rabb_ter[i+1][j] == 1:
                    if j+1 < m and rabb_ter[i+1][j+1] == rabb_ter[i][j+1] == 1:
                        sq3 = True
                    if rabb_ter[i+1][j-1] == rabb_ter[i][j-1] == 1:
                        sq4 = True
                if sq1 and sq2 and sq3 and sq4:
                    hand1 = check_round_sqvr(i + 2, j + 2, rabb_ter, 4)
                if sq2:
                    hand2 = check_round_sqvr(i - 1, j + 2, rabb_ter, 3)
                if sq3:
                    hand3 = check_round_sqvr(i + 2, j + 2, rabb_ter, 3)
                if sq4:
                    hand4 = check_round_sqvr(i - 2, j + 1, rabb_ter, 3)

                hand = sorted([hand1, hand2, hand3, hand4])[-1]
                mhand = max(hand[0], mhand)

                if hand[0] > max(m, n) / 2:
                    return (hand[0])

                elif hand[0] > 50:
                    return(max(mhand, check_matrix(hand[1] - hand[0]-1, hand[1]+1, hand[2], m, mhand), check_matrix(hand[1]-1, n, 1, m, mhand)))

    return(mhand)


n, m = map(int, input().split())
rabb_ter = [list(map(int, input().split())) for _ in range(n)]

print(check_matrix(1,n,1,m, 0))

"""