from time import sleep
from datetime import datetime


class TrafficLight:
    __color: list
    colors = {'red': 7, 'yellow': 2, 'green': 3}

    def __init__(self, color: list):
        self.__color = color

    def running(self):
        if self.__color != list(self.colors.keys()):
            print('Сбой в работе светофора!')
        else:
            for item in self.__color:
                minutes = '{:02d}'.format(datetime.now().minute)
                seconds = '{:02d}'.format(datetime.now().second)
                print(f'{minutes}:{seconds}   {item}')
                sleep(self.colors.get(item))


tlNorm = TrafficLight(['red', 'yellow', 'green'])
tlBad = TrafficLight(['red', 'green', 'yellow'])
for i in range(0, 3):
    tlNorm.running()
tlBad.running()
