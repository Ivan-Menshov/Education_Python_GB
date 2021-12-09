class ScladOrgtexnic:
    def __init__(self, product_list):
        self.product_list = product_list

    def get_gadget(self, gadget):
        if type(gadget) == list:
            return self.product_list.extend(gadget)
        else:
            return self.product_list.append(gadget)

    def get_gadget_to_company(self, gadget, company_name):
        if self.product_list.count(gadget) > 0:
            self.product_list.remove(gadget)
            print(f'В {company_name} отправлен {gadget}')
        else:
            print(f'На складе нет данного товара!')


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


my_scaner1 = Scaner('Samsung_G21', '1200*800')
my_scaner2 = Scaner('Samsung_G22', '1400*1000')
my_scaner3 = Scaner('Samsung_G33', '1900*1200')

my_printer_1 = Printer('Samsung_GTR_22', False)
my_printer_2 = Printer('Samsung_GTR_22_c', True)

my_kseroks1 = Kseroks('Samsung_md21_c', True, '1900*1200')

sclad = ScladOrgtexnic([])
sclad.get_gadget([my_scaner1, my_scaner2, my_scaner3, my_printer_1, my_printer_2, my_kseroks1])
print(sclad.product_list)

my_kseroks2 = Kseroks('Samsung_md22_c', False, '1200*800')
sclad.get_gadget(my_kseroks2)
print(sclad.product_list)

sclad.get_gadget_to_company(my_printer_1, 'Apple')
print(sclad.product_list)
