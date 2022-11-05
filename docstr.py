from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def sqrts(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(yournumber):
    """Проверяет что число не равно нулю."""
    if yournumber <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: number')


print(message)
calc(25.5)