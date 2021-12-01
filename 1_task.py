class TrafficLight:

    def __init__(self, __color):
        self.__color = __color

    def running(self):
        import time
        print(self.__color)
        while True:
            if self.__color == 'RED':
                time.sleep(7)
                self.__color = 'YELLOW'
                print(self.__color)
            elif self.__color == 'YELLOW':
                time.sleep(2)
                self.__color = 'GREEN'
                print(self.__color)
            else:
                time.sleep(10)
                self.__color = 'RED'
                print(self.__color)


my_color = TrafficLight('RED')
TrafficLight.running(my_color)
