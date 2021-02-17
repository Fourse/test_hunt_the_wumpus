from abc import ABC


class Weapon(ABC):
    def __init__(self, name):
        self.name = name


class Bow(Weapon):
    def __init__(self):
        super().__init__(name='bow')
        self.arrows = 5


class Sword(Weapon):
    def __init__(self):
        super().__init__(name='sword')
