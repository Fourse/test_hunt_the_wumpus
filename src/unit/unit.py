from abc import ABC


class Unit(ABC):
    def __init__(self, name, special):
        self.name = name
        self.special = special


class Player(Unit):
    def __init__(self, name, special, inventory):
        super().__init__(name, special)
        self.inventory = inventory


class Wumpus(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)


class Bat(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)


class Pit(Unit):
    # yeah, it`s unit too
    def __init__(self, name, special):
        super().__init__(name, special)
