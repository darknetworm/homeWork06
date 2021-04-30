class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title.title()} - ручка'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title.title()} - карандаш'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title.title()} - фломастер'


ruler = Stationery('линейка')
redPen = Pen('bic')
greyPencil = Pencil('koh-i-noor')
greenHandle = Handle('Berlingo')

print(ruler.draw())
print(redPen.draw())
print(greyPencil.draw())
print(greenHandle.draw())
