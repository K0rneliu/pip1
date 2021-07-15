#lesson7Task2


from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param =param

    @property
    @abstractmethod
    def consumation(self):
        pass

    def __add__(self, other):
        self.result +=self.consumation + other.consumation
        return Costume(0)

    def __str__(self):
        res = self.result
        self.result = 0
        return f"{res}"
    class Coat(self):
        @property
        def consumation(self):
            return round(self.param / 6.5) + 0.5

    class Costume(self):
        @property
        def consumation(self):
            return round((2*self.param + 0.3) / 100)


    coat = Coat(42)
    costume = Costume(170)
    print(coat + costume + coat)


