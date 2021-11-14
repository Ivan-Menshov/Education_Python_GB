def sum_numb(numb, stop):
    num_list = numb.split(' ')
    sum_list = 0
    for elem in num_list:
        if elem == stop:
            break
        sum_list += float(elem)
    return sum_list


stop = '!'
s = 0
while True:
    user_str = input('Введите числа через пробел: ')
    s += sum_numb(user_str, stop)
    print(f'Summa = {s}')
    if stop in user_str:
        break
