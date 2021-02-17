from abc import ABC

from src.exceptions.exceptions import WonGame
from src.exceptions.exceptions import LostGame

from src.inventory.weapon import Bow


class Unit(ABC):
    def __init__(self, name, special):
        self.name = name
        self.special = special

    def action(self, action):
        raise NotImplementedError


class Player(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)
        self.inventory = {}
        self.alive = True

    def inventory_interaction(self):
        self.inventory['weapon'] = Bow()

    def action(self, action):
        pass

    def __del__(self):
        if self.alive is False:
            raise LostGame


class Wumpus(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)
        self.sleep = True
        self.alive = True

    def action(self, action):
        pass

    def __del__(self):
        if self.alive is False:
            raise WonGame


class Bat(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)

    def action(self, action):
        pass


class Pit(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)

    def action(self, action):
        pass
