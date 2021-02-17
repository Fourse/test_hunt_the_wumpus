from src.world.world_rework import World

from src.display.display_rework import Display

from src.exceptions.exceptions import WonGame
from src.exceptions.exceptions import LostGame


class GameLogic:
    def process_action(self, world, display):
        display.add_data(f'{"-" * 59}')
        display.add_data('Attack [a] or Move [m]?')
        action = display.await_input()
        if action == 'm':
            self.move(world, display)
        elif action == 'a':
            self.attack(world, display)
        else:
            pass

    def move(self, world, display):
        display.change_last_data('Where you go?')
        room = display.await_input()
        try:
            room = int(room)
        except ValueError:
            self.move(world, display)
        self.process_move(world, display)
        display.clear_msg()

    def process_move(self, world, display):
        world.rooms[world.player_pos].who_in.action('move')

    def attack(self, world, display):
        print('aga')
        raise WonGame

    def check_cur_room(self, world, display):
        display.add_data(f'You in {world.player_pos}')
        display.add_data(f'Paths in the room lead to rooms: {world.rooms[world.player_pos].ways_to}')

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
                self.display.clear_msg()
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
