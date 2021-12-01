class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина сменла направление. Тепрь она едет {0}'.format(direction))

    def show_speed(self):
        print(f'Ваша скорость - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Сбавь скорость шумахер')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Сбавь скорость шумахер')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


class SportCar(Car):
    pass


town_car = TownCar(88, 'black', 'BWW')
sport_car = SportCar(130, 'red', 'Maserati')
police_car = PoliceCar(120, 'white', 'Lada')
work_car = WorkCar(44, 'balck', 'Honda')

town_car.show_speed()
sport_car.show_speed()
police_car.show_speed()
work_car.show_speed()

town_car.go()
sport_car.stop()
police_car.turn('Прямо')
work_car.turn('Налево')
