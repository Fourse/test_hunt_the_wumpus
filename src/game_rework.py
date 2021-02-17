from src.world.world_rework import World

from src.display.display_rework import Display

from src.exceptions.exceptions import WonGame
from src.exceptions.exceptions import LostGame


class GameLogic:
    def process_action(self, world, display):
        action = display.await_input()
        if action == 'move':
            self.move(world, display)
        elif action == 'attack':
            self.attack(world, display)

    def move(self, world, display):
        pass

    def attack(self, world, display):
        pass

    def check_cur_room(self, world, display):
        pass

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
                game_logic.check_next_rooms(self.world, self.display)
                game_logic.process_action(self.world, self.display)
            except KeyboardInterrupt:
                exit(0)
            except WonGame:
                self.display.end_game('won', 'some msg')
                break
            except LostGame:
                self.display.end_game('lost', 'some msg')
                break
