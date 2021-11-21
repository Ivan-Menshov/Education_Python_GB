my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('task_files/task_4_1.txt', 'r', encoding='utf-8') as file:
    info = file.read().split('\n')
    info = [i.split(' ') for i in info]

with open('task_files/task_4_2.txt', 'w', encoding='utf-8') as file:
    for i in info:
        file.write(f'{my_dict[i[0]]} {i[1]} {i[2]}\n')
