with open('task_files/task_2.txt', 'r', encoding='utf-8') as file:
    my_strings = file.readlines()
    print(f'В данном файле {len(my_strings)} строк(и).\n')
    print(r'Подсчет срок выполнен без учета спецсивола "\n". ','\n')
    for i in range(len(my_strings)):
        print(my_strings[i][:len(my_strings[i])-1])
        print(f'В {i+1} строке {len(my_strings[i])-1} символов.\n')
