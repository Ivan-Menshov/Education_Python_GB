cash = float(input('Введите выручку: '))
spend = float(input('Введите издержеки: '))
if cash > spend:
    print('Фирма работает в прибыль')
    print('Рентабельность выручки: ', (cash-spend)/cash)
    numbers = int(input('Введите количесвто сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника:', (cash-spend)/numbers)
elif cash < spend:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
