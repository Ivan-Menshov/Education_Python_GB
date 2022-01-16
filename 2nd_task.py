time_in_sec = int(input('Введите время в секундах: '))
if time_in_sec < 0:
    print('Хватит прикалываться, время не может быть отрицательным, МЫ ЖЕ НЕ НА ФИЗМАТЕ!!!')
else:
    sec = time_in_sec % 60
    minutes = time_in_sec//60
    hour = minutes//60
    print(f'{hour:02}:{(minutes-60*hour):02}:{sec:02}')
