def my_func(x, y, z):
    summa = x+y+z
    return summa - min(x, y, z)


x = float(input('Введите 1 число: '))
y = float(input('Введите 2 число: '))
z = float(input('Введите 3 число: '))
print(my_func(x, y, z))
