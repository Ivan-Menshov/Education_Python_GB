with open('task_files/task_3.txt', 'r', encoding='utf-8') as file:
    workers = file.readlines()
    workers = [i[:len(i) - 1].split() for i in workers]
    low_workers = [i[0] for i in workers if int(i[1]) < 20000]
    print(f'Список работников с окладом менее 20000 рублей: {low_workers}.')
    mean = 0
    for i in workers:
        mean += int(i[1])
    print(f'Средний оклад работников: {round(mean/len(workers),2)} рублей.')
