with open('task_files/task_6.txt', 'r', encoding='utf-8') as file:
    info = file.read().split('\n')
    keys = [i[:i.find(':')] for i in info]
    numbers = [str(i) for i in range(10)]
    values = []
    summa = 0
    string_i = ''
    for i in info:
        for j in range(len(i)):
            if i[j] in numbers:
                string_i += i[j]
            if (string_i != '') and (i[j] not in numbers):
                summa += int(string_i)
                string_i = ''
        values.append(summa)
        summa = 0
    my_dictionary = dict(zip(keys, values))
    print(my_dictionary)
