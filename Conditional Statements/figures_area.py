from math import pi


def calcArea(figure):
    area = 0
    if figure == 'square':
        side = float(input())
        area = side ** 2
    elif figure == 'rectangle':
        a = float(input())
        b = float(input())
        area = a * b
    elif figure == 'circle':
        r = float(input())
        area = pi * r ** 2
    elif figure == 'triangle':
        a = float(input())
        h = float(input())
        area = a * h / 2
    return f'{area:.3f}'


user_input = input()
print(calcArea(user_input))

