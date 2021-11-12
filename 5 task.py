my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число:'))
for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        break
    if number < my_list[-1]:
        my_list.append(number)
print(my_list)
