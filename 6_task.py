from itertools import cycle, count
stop = 10
my_list = [i for i in range(3)]
my_count = count()
my_cycle = cycle(my_list)
print([next(my_count) for i in range(stop)])
print([next(my_cycle) for i in range(stop)])
