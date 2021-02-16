from abc import ABC
from typing import Any

from src.utils.text_manager import TextManager
from src.utils.exceptions import WonGame, LostGame


class Unit(ABC):
    def __init__(self, name, special):
        self.name = name
        self.special = special

    def move(self):
        raise NotImplementedError

    def attack(self):
        raise NotImplementedError


class Player(Unit):
    def __init__(self, name, special, inventory):
        super().__init__(name, special)
        self.inventory = inventory

    def move(self):
        print(TextManager.player_moves())

    def attack(self):
        print(TextManager.player_attacks())


class Wumpus(Unit):
    def __init__(self, name, special, sleep=True):
        super().__init__(name, special)
        self.sleep = sleep

    def move(self):
        if self.sleep is True:
            return True
        return False

    def attack(self):
        print(TextManager.you_has_been_killed())
        raise LostGame


class Bat(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)

    def move(self):
        pass

    def attack(self):
        pass


class Pit(Unit):
    # yeah, it`s unit too
    def __init__(self, name, special):
        super().__init__(name, special)

    def move(self):
        pass

    def attack(self):
        print(TextManager.you_fell_down())
        raise LostGame
