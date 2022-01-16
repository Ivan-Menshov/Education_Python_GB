number = int(input('Введите число: '))
number_max = 0
while number > 0:
    last_number = number%10
    if last_number > number_max:
        number_max = last_number
    number = number//10
print(number_max)
