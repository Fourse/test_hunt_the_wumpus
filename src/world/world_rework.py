import random

import networkx as nx

from src.unit.unit_rework import Player
from src.unit.unit_rework import Wumpus
from src.unit.unit_rework import Bat
from src.unit.unit_rework import Pit


class Room:
    def __init__(self, ways_to, state="empty", who_in=None):
        self.ways_to = ways_to
        self.state = state
        self.who_in = who_in

    def process_who_in_special(self, display):
        try:
            if self.who_in.special == 'smell':
                display.add_data('Smell like a stinky socks...')
            elif self.who_in.special == 'noise':
                display.add_data('It`s because: I AM BATMAN')
            elif self.who_in.special == 'wind':
                display.add_data('Watch your step')
        except AttributeError:
            return


class World:
    def __init__(self):
        self.player_pos = 0
        self.wumpus_pos = 0
        self.rooms = {}
        self.unit_list = [
            Bat('bat', 'noise'),
            Bat('bat', 'noise'),
            Pit('pit', 'wind'),
            Pit('pit', 'wind'),
            Player('player', None),
            Wumpus('wumpus', 'smell')
        ]

    def gen_map(self):
        graph = nx.random_regular_graph(3, 20)
        for node in graph:
            self.rooms[node] = Room(ways_to=[link for link in graph[node].keys()])

    def fill_map(self):
        empty_rooms = self.get_empty_rooms()
        for unit in self.unit_list:
            rand_room = random.choice(empty_rooms)
            if unit.name == 'player':
                self.player_pos = rand_room
            elif unit.name == 'wumpus':
                self.wumpus_pos = rand_room
            self.fill_room(rand_room, 'occupied', unit)
            empty_rooms.remove(rand_room)

    def get_empty_rooms(self):
        empty_rooms = list()
        for room in self.rooms:
            if self.rooms[room].state == 'empty':
                empty_rooms.append(room)

        return empty_rooms

    def fill_room(self, room, state, unit):
        self.rooms[room].state = state
        self.rooms[room].who_in = unit
