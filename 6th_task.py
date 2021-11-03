start_val = float(input('Введите результат пробежки первого дня(км): '))
end_val = float(input('Введите желаемый результат (км): '))
day = 1
while True:
    if start_val >= end_val:
        print(f'Вы достигнете результата на {day} день')
        break
    start_val *= 1.1
    day += 1
