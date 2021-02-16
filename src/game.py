import random

from src.world.world import EasyWorld
from src.world.world import MediumWorld
from src.world.world import HellWorld

from src.utils.utils import TextManager
from src.utils.exceptions import EndGame


def quit_game():
    print(TextManager.quit())
    exit(0)


class GameLogic:
    def __init__(self, world, cur_room):
        self.world = world
        self.cur_room = cur_room

    def _change_room_status(self):
        pass

    def check_cur_room(self):
        who_in = self.world.rooms[self.cur_room].who_in
        if who_in.name == 'wumpus':
            pass
        elif who_in.name == 'bat':
            pass
        elif who_in.name == 'pit':
            pass
        else:
            # print('fuh, proneslo\n')
            pass

    def check_next_rooms(self):
        next_rooms = self.world.rooms[self.cur_room].ways_to
        for room in next_rooms:
            self.world.rooms[room].process_special()

    def process_action(self):
        try:
            action = input(TextManager.await_action()).lower()
            if action == 'a':
                pass
            elif action == 'm':
                pass
            else:
                print(TextManager.give_try())
                self.process_action()
        except KeyboardInterrupt:
            quit_game()


class Game:
    def __init__(self):
        self.prepare_game()

    def _choose_difficulty(self):
        ok_status = ['easy', 'medium', 'hell']
        try:
            diff = input(TextManager.choose_difficulty()).lower()
            if diff in ok_status:
                return diff
            elif diff == 'h' or diff == 'help':
                print(TextManager.game_rules())
                self._choose_difficulty()
            elif diff == 'q':
                quit_game()
            else:
                raise ValueError
        except KeyboardInterrupt:
            quit_game()
        except ValueError:
            print(TextManager.give_try())
            self._choose_difficulty()

    @staticmethod
    def _create_world(difficulty):
        if difficulty == 'easy':
            world = EasyWorld(20, 3)
        elif difficulty == 'medium':
            world = MediumWorld(20, 3)
        elif difficulty == 'hell':
            world = HellWorld(20, 3)
        else:
            world = EasyWorld(20, 3)
        return world

    def prepare_game(self):
        print(TextManager.game_rules())
        difficulty = self._choose_difficulty()
        world = self._create_world(difficulty)
        print(TextManager.start_game())
        world.gen_units()
        world.gen_map()
        start_room = world.fill_map()
        self.game_logic = GameLogic(world, start_room)

    def run(self):
        while True:
            try:
                self.game_logic.check_cur_room()
                self.game_logic.check_next_rooms()
                self.game_logic.process_action()
                # pass
            except KeyboardInterrupt:
                quit_game()
            except EndGame:
                print('oooooops')
                break
