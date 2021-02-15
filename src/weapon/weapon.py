from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self):
        pass


class Bow(Weapon):
    def __init__(self):
        super().__init__()
