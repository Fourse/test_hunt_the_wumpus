import time
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

    def inventory_interaction(self):
        self.inventory['weapon'] = Bow()

    def action(self, action):
        if action == 'move':
            print('Ok, let`s go..')
            time.sleep(1)
        elif action == 'attack':
            print('Pulling the string..')
            time.sleep(1)


class Wumpus(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)
        self.sleep = True

    def action(self, action):
        if action == 'move':
            print()
        elif action == 'attack':
            print('Hmm, lunch')
            time.sleep(1)
            raise LostGame


class Bat(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)

    def action(self, action):
        print('I believe, I can fly')
        time.sleep(1)
        print('Oh, where I am?')
        time.sleep(1)


class Pit(Unit):
    def __init__(self, name, special):
        super().__init__(name, special)

    def action(self, action):
        print('AAAAAAAAAAaaaaaa')
        time.sleep(1)
        raise LostGame
