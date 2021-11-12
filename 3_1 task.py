month = [['12', '1', '2'], ['3', '4', '5'], ['6', '7', '8'], ['9', '10', '11']]
user_month = str(input('Введите номер месяца: '))
if user_month in month[0]:
    print ('Зима')
if user_month in month[1]:
    print ('Весна')
if user_month in month[2]:
    print ('Лето')
if user_month in month[3]:
    print ('Осень')
