class ScladOrgtexnic:
    def __init__(self, product_list):
        self.product_list = product_list


class Orgtexnic:
    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return f'{self.model}'


class Printer(Orgtexnic):
    def __init__(self, model, color):
        super().__init__(model)
        self.color = color


class Scaner(Orgtexnic):
    def __init__(self, model, accuracy):
        super().__init__(model)
        self.accuracy = accuracy


class Kseroks(Orgtexnic):
    def __init__(self, model, color, accuracy):
        super().__init__(model)
        self.color = color
        self.accuracy = accuracy


my_scaner1 = Scaner('Sumsung_G21', '1200*800')
my_scaner2 = Scaner('Sumsung_G22', '1400*1000')
my_scaner3 = Scaner('Sumsung_G33', '1900*1200')

my_printer_1 = Printer('Sumsung_GTR_22', False)
my_printer_2 = Printer('Sumsung_GTR_22_c', True)

my_kseroks = Kseroks('Sumsung_md21_c', True, '1900*1200')

sclad = ScladOrgtexnic([my_scaner1, my_scaner2, my_scaner3, my_printer_1, my_printer_2, my_kseroks])

print(sclad.product_list)
