from abc import ABC


class Weapon(ABC):
    def __init__(self, name):
        self.name = name


class Bow(Weapon):
    def __init__(self, name):
        super().__init__(name)
        self.arrows = 5
