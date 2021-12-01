class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def weight(self, massa, tolshina):
        return massa * tolshina * self._width * self._lenght


my_road = Road(20, 5000)
print(my_road._lenght)
print(my_road._width)
print(my_road.weight(25, 5))
