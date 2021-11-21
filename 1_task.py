with open('task_files/task_1.txt', 'w', encoding='utf-8') as file:
    while True:
        user_str = str(input('Введите строку: '))
        if user_str == '':
            break
        else:
            file.write(user_str+'\n')
