from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self):
        pass


class Player(Unit):
    def __init__(self):
        super().__init__()


class Wumpus(Unit):
    def __init__(self):
        super().__init__()


class Bat(Unit):
    def __init__(self):
        super().__init__()