import json

with open('task_files/task_7.txt', 'r', encoding='utf-8') as file:
    info = file.read().split('\n')
    info = [i.split() for i in info]
    keys = []
    values = []
    summa = 0
    for i in info:
        keys.append(i[0])
        values.append(float(i[2]) - float(i[3]))
        summa += float(i[2]) - float(i[3])
    my_dictionary = dict(zip(keys, values))
    my_dictionary_1 = {'average_profit': summa / len(values)}
    my_list = [my_dictionary, my_dictionary_1]

with open('task_files/task_7.json', 'w', encoding='utf-8') as file:
    json.dump(my_list, file)
