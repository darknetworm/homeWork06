from datetime import datetime
from time import sleep


class TrafficLight:
    __color: str
    colors = {'red': 7, 'yellow': 2, 'green': 3}
    count = 0

    def __init__(self, color: str):
        self.__color = color

    def running(self):
        if self.__color == list(self.colors.keys())[self.count]:
            minutes = '{:02d}'.format(datetime.now().minute)
            seconds = '{:02d}'.format(datetime.now().second)
            print(f'{minutes}:{seconds}   {self.__color}')
            sleep(self.colors.get(self.__color))
            TrafficLight.count += 1
            if TrafficLight.count == 3:
                TrafficLight.count = 0
        else:
            exit('Сбой в работе светофора')


tlRed = TrafficLight('red')
tlYellow = TrafficLight('yellow')
tlGreen = TrafficLight('green')
for i in range(0, 3):
    tlRed.running()
    tlYellow.running()
    tlGreen.running()
tlRed.running()
tlGreen.running()
