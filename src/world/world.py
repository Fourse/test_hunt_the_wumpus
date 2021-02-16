import random

from abc import ABC
from typing import Any

import networkx as nx

from src.unit.unit import Player
from src.unit.unit import Wumpus
from src.unit.unit import Bat
from src.unit.unit import Pit

from src.inventory.weapon import Bow


class Room:
    def __init__(self, number, ways_to, state="empty", who_in=None, special=None):
        self.number = number
        self.ways_to = ways_to
        self.state = state
        self.who_in = who_in
        self.special = special

    def process_special(self):
        if self.special == 'smell':
            print('hmm, wumpus is nearby\n')
        elif self.special == 'noise':
            print('I AM BATMAN\n')
        elif self.special == 'wind':
            print('look under ur feet\n')
        else:
            pass


class World(ABC):
    def __init__(self, room_count, way_count):
        self.room_count = room_count
        self.way_count = way_count
        self.player_inventory = dict()
        self.unit_list = None
        self.rooms = {}

    def gen_map(self):
        graph = nx.random_regular_graph(3, 20)
        for node in graph:
            self.rooms[node] = Room(node, [link for link in graph[node].keys()])

    def fill_room(self, room, state, unit, special):
        self.rooms[room].state = state
        self.rooms[room].who_in = unit
        self.rooms[room].special = special

    def get_empty_rooms(self):
        empty_rooms = list()
        for room in self.rooms:
            if self.rooms[room].state == 'empty':
                empty_rooms.append(room)

        return empty_rooms

    def fill_map(self):
        empty_rooms = self.get_empty_rooms()
        start_room = 0
        for unit in self.unit_list:
            rand_room = random.choice(empty_rooms)
            if unit.name == 'player':
                start_room = rand_room
            self.fill_room(rand_room, 'occupied', unit, unit.special)
            empty_rooms.remove(rand_room)
        return start_room

    def gen_units(self):
        raise NotImplementedError

    def create_unit_list(self, any: Any):
        raise NotImplementedError


class EasyWorld(World):
    def __init__(self, room_count, way_count):
        super().__init__(room_count, way_count)

    def gen_units(self):
        self.player_inventory['weapon'] = Bow
        self.create_unit_list(self.player_inventory)

    def create_unit_list(self, inventory):
        self.unit_list = [
            Bat('bat', 'noise'),
            Bat('bat', 'noise'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Player('player', None, inventory),
            Wumpus('wumpus', 'smell', True)
        ]


class MediumWorld(World):
    def __init__(self, room_count, way_count):
        super().__init__(room_count, way_count)

    def gen_units(self):
        self.player_inventory['weapon'] = Bow
        self.create_unit_list(self.player_inventory)

    def create_unit_list(self, inventory):
        self.unit_list = [
            Bat('bat', 'noise'),
            Bat('bat', 'noise'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Player('player', None, inventory),
            Wumpus('wumpus', 'smell')
        ]


class HellWorld(World):
    def __init__(self, room_count, way_count):
        super().__init__(room_count, way_count)

    def gen_units(self):
        self.player_inventory['weapon'] = Bow
        self.create_unit_list(self.player_inventory)

    def create_unit_list(self, inventory):
        self.unit_list = [
            Bat('bat', 'noise'),
            Bat('bat', 'noise'),
            Bat('bat', 'noise'),
            Bat('bat', 'noise'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Player('player', None, inventory),
            Wumpus('wumpus', 'smell')
        ]
