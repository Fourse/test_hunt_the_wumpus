from abc import ABC
from typing import Any

from src.utils.text_manager import TextManager
from src.utils.exceptions import WonGame, LostGame
from src.utils.exceptions import WumpusDead


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
        if self.inventory['weapon'].name == 'bow':
            self.inventory['weapon'].arrows -= 1
            if self.inventory['weapon'].arrows == 0:
                print(TextManager.empty_quiver())
                raise LostGame


class Wumpus(Unit):
    def __init__(self, name, special, sleep=True):
        super().__init__(name, special)
        self.sleep = sleep
        self.alive = True

    def move(self):
        if self.sleep is True:
            return True
        return False

    def attack(self):
        print(TextManager.you_has_been_killed())
        raise LostGame

    def __del__(self):
        if self.alive is False:
            print('AAAARGH')
            print(TextManager.won_the_game())


class Bat(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)

    def move(self):
        print(TextManager.fly_with_bat())

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
