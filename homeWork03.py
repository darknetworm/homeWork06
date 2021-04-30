class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.position} {self.name.title()} {self.surname.title()}'

    def get_total_income(self):
        return 'имеет оклад {} Пиастров'.format(self._income.get('wage') + self._income.get('bonus'))


vasil = Position('василий', 'алибабаев', 'инженер', 3500.12, 1000)
eugen = Position('Евгений', 'габрилян', 'шутник', 52000, 12000)
solist = Position('юрий', 'заковаев', 'певец', 16000, 5000)
print(vasil.get_full_name(), vasil.get_total_income())
print(eugen.get_full_name(), eugen.get_total_income())
print(solist.get_full_name(), solist.get_total_income())
