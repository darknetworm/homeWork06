class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = 'right'

    def go(self):
        return f'{self.color.title()} {self.name.title()} go'

    def stop(self):
        return f'{self.color.title()} {self.name.title()} stop'

    def turn(self):
        return f'{self.color.title()} {self.name.title()} turn to the {self.direction}'

    def show_speed(self):
        return f'{self.color.title()} {self.name.title()} speed is {self.speed} km/h'


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str, speed_limit: int = 60):
        super().__init__(speed, color, name, is_police=0)
        self.speed_limit = speed_limit

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'WARNING {self.color.upper()} {self.name.upper()}! Max speed is {self.speed_limit} km/h')
        return f'{self.color.title()} {self.name.title()} speed is {self.speed} km/h'


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, is_police=0)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str, speed_limit: int = 40):
        super().__init__(speed, color, name, is_police=0)
        self.speed_limit = speed_limit

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'WARNING {self.color.upper()} {self.name.upper()}! Max speed is {self.speed_limit} km/h')
        return f'{self.color.title()} {self.name.title()} speed is {self.speed} km/h'


class PoliceCar(Car):
    def __init__(self, speed: int, name: str, color='police', ):
        super().__init__(speed, color, name, is_police=1)


skoda = PoliceCar(20, 'skoda')
renault = TownCar(65, 'red', 'renault')
dodge = SportCar(120, 'Orange', 'dodge')
garbage = WorkCar(41, 'white', 'MAN')
print(skoda.stop())
print(renault.show_speed())
print(dodge.turn())
print(garbage.show_speed())
