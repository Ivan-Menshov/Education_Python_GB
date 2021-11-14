def info_user(name, surname, year, city, email, phone):
    return f'{name} {surname} {year} {city} {email} {phone}'


a = input('Name: ')
b = input('Surname: ')
c = input('Year: ')
d = input('City: ')
e = input('Email: ')
f = input('Phone: ')

print(info_user(name =a, surname=b, year=c, city=d, email=e, phone=f))
