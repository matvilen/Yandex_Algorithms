"""
Ограничение времени	- 1 секунда
Ограничение памяти	- 64Mb

Рассмотрим последовательность, состоящую из круглых, квадратных и
фигурных скобок. Программа должна определить, является ли данная
скобочная последовательность правильной. Пустая последовательность
является правильной. Если A — правильная, то последовательности
(A), [A], {A} — правильные. Если A и B — правильные последовательности,
то последовательность AB — правильная.

Формат ввода
В единственной строке записана скобочная последовательность,
содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести
строку "yes", иначе строку "no".

Пример 1
Ввод
()[]
Вывод
yes

Пример 2
Ввод
([)]
Вывод
no

Пример 3
Ввод
(
Вывод
no
"""

sq_dict = {'[':']', '(':')', '{':'}'}
check_close = []
is_right = True

for i, el in enumerate(input()):
    #если скобка открывающая, то добавим закрывающую ее в check_close
    if el in ('[', '(', '{'):
        check_close.append(sq_dict[el])
    # если скобка закрывающая и при этом совпадает с последним закр-м эл-ом,
    # то удаляем посл. эл-т, считая эту часть закр-й и двигаемся дальше
    elif len(check_close) > 0 and check_close[-1] == el:
        check_close.pop()
    else:
        is_right = False
        break
print('yes' if is_right and len(check_close) == 0 else 'no')