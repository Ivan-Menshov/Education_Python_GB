class My_Error(Exception):
    def __init__(self, taxt):
        self.text = taxt


my_list = []
while True:
    try:
        list_elem = input(f'Введите элемент списка: ')
        if list_elem == 'stop':
            print(my_list)
            break
        if not list_elem.isdigit():
            raise My_Error('В список вносятся только числа!')
        else:
            my_list.append(list_elem)
    except My_Error as text:
        print(text)
