import random

from src.world.world_rework import World

from src.display.display_rework import Display

from src.exceptions.exceptions import WonGame
from src.exceptions.exceptions import LostGame


class GameLogic:
    def process_action(self, world, display):
        display.change_footer(f'{"-" * 59}')
        display.change_footer('Attack [a] or Move [m]?')
        action = display.await_input()
        if action == 'm':
            self.move(world, display)
        elif action == 'a':
            self.attack(world, display)
        else:
            pass

    def move(self, world, display):
        display.clear_footer()
        display.change_footer('Where you go?')
        room = display.await_input()
        try:
            room = int(room)
            self.process_move(world, display, room)
        except ValueError:
            self.move(world, display)

    def process_move(self, world, display, room):
        world.rooms[world.player_pos].who_in.action('move')
        where_go = world.rooms[room]
        try:
            if room == world.wumpus_pos:
                world.rooms[world.wumpus_pos].who_in.action('attack')
            elif where_go.who_in.name == 'bat':
                where_go.who_in.action('')
                empty_rooms = world.get_empty_rooms()
                self._moving_between_rooms(world, random.choice(empty_rooms), room, where_go.who_in)
                room = random.choice(list(world.rooms.keys()))
            elif where_go.who_in.name == 'pit':
                where_go.who_in.action('fall')
        except AttributeError:
            pass
        if room != world.player_pos:
            self._moving_between_rooms(world, room, world.player_pos, world.rooms[world.player_pos].who_in)
        world.player_pos = room

    @staticmethod
    def _moving_between_rooms(world, _to, _from, who_in):
        world.fill_room(
            _to,
            'occupied',
            who_in,
        )
        world.fill_room(
            _from,
            "empty",
            None,
        )

    def attack(self, world, display):
        print('aga')
        raise WonGame

    @staticmethod
    def check_cur_room(world, display):
        display.change_main_data(f'You in {world.player_pos}')
        display.change_main_data(f'Paths in the room lead to rooms: {world.rooms[world.player_pos].ways_to}')

    @staticmethod
    def check_next_rooms(world, display):
        next_rooms = world.rooms[world.player_pos].ways_to
        for next_room in next_rooms:
            world.rooms[next_room].process_who_in_special(display)


class Game:
    def __init__(self):
        self.world = None
        self.display = None

    def create_world(self):
        self.world = World()
        self.world.gen_map()
        self.world.fill_map()

    def load_game(self):
        self.display = Display()
        self.create_world()

    def run(self):
        game_logic = GameLogic()
        while True:
            try:
                game_logic.check_cur_room(self.world, self.display)
                game_logic.check_next_rooms(self.world, self.display)
                game_logic.process_action(self.world, self.display)
                self.display.clear_main()
            except KeyboardInterrupt:
                exit(0)
            except WonGame:
                self.display.clear()
                print('Congrats dude')
                break
            except LostGame:
                self.display.clear()
                print('WASTED')
                break
