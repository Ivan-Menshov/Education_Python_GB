input_list = str(input('Введите список через пробел: '))
my_list = input_list.split()
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)