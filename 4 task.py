def my_func_1(x, y):
    return x**y

def my_func_2(x, y):
    y = y*-1
    rez = 1
    while y>0:
        rez *=x
        y -= 1
    return 1 / rez


x = float(input('Введите число: '))
y = int(input('Введите степень числа(отрицательная): '))
print(my_func_1(x, y))
print(my_func_2(x, y))
