#lesson6Task3


class Car:
    '''Auto'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f' new car: {self.name} (color {self.color}) auto_1 - {self.is_police}')

    def go(self):
        print(f'{self.name}: Auto go.')

    def stop(self):
        print(f'{self.name}: Auto stop.')

    def turn(self):
        print(f'{self.name}: Auto turn.')

    def show_speed(self):
        return f'{self.name} Speed auto: {self.speed}'


class TownCar(Car):
    '''TownCar'''

    def show_speed(self):
        return f'{self.name} Speed auto: {self.speed}. speeding!'\
            if self.speed > 60 else f'{self.name}: Speed auto {self.speed}'


class WorkerCar(Car):
    '''WorkerCar'''

    def show_speed(self):
        return f'{self.name} Speed auto: {self.speed}. speeding!'\
            if self.speed > 40 else f'{self.name}: Speed auto {self.speed}'


class PoliceCar(Car):
    '''PoliceCar'''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar( 'PoliceCar',  'Red', 80)
police_car.go()
