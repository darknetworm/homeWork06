class Road:
    _length: int
    _width: int
    thickAsf: int = 5

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def weightAsf(self):
        return (self._length * self._width * 25 * self.thickAsf) / 1000


try:
    userLn = int(input('Введите длину дорожного полотнав метрах: '))
    userWd = int(input('Введите ширину дорожного полотна: '))
except ValueError:
    exit('Введенные данные не числа')

arbat = Road(userLn, userWd)
print(
    f'Масса асфальта, необходимого для покрытия дорожного полотна толщиной {Road.thickAsf} см равна {round(arbat.weightAsf())} т')
