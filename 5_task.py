class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки', self.title)


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой - ', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашиком - ', self.title)


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером - ', self.title)


pen = Pen('Crauser')
pencil = Pencil('Croher')
handle = Handle('Marker')
pen.draw()
pencil.draw()
handle.draw()
