with open('task_files/task_5.txt', 'w', encoding='utf-8') as file:
    my_string = str(input('Введиче чила через пробел: '))
    numbers = my_string.split()
    summa = 0
    for i in numbers:
        summa += float(i)
    print(f'Сумма чисел в строке = {summa}')
    file.write(my_string)
