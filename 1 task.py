def delenie(x, y):
    try:
        rez = x/y
    except ZeroDivisionError:
        rez = 'Внимание! Делеение на 0!'
    return rez


x = float(input('Введите делимое: '))
y = float(input('Введите делитель: '))

print(delenie(x, y))
