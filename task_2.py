from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def total_material(self):
        pass


class Palto(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def total_material(self):
        return self.v / 6.5 + 0.5


class Kostume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def total_material(self):
        return self.h * 2 + 0.3

    def total_sum(self, my_list):
        sum = 0
        for i in my_list:
            sum += i.total_material
        return sum


coat = Palto(60)
costume = Kostume(3.14)
costume_1 = Kostume(3.14)
my_list = [coat, costume, costume_1]
print(coat.total_material)
print(costume.total_material)
print(costume.total_sum(my_list))
