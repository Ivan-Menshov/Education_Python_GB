input_list = str(input('Введите список через пробел: '))
my_list = input_list.split()
for i in range(len(my_list)):
    if len(my_list[i])>10:
        print(f'{i+1}) {my_list[i][:10]}')
    else:
        print(f'{i+1}) {my_list[i]}')
