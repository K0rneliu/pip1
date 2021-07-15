#lesson6Task3


class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': salary, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'

manager = Position('Ion', 'Eva', 'CEO', 10000, 6000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())