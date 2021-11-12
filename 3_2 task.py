seasons = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}
user_month = str(input('Введите номер месяца: '))
for keys in seasons:
    if user_month in seasons[keys]:
        print(keys)
