import random

from src.world.world import EasyWorld
from src.world.world import MediumWorld
from src.world.world import HellWorld

from src.utils.exceptions import EndGame


class GameLogic:
    def __init__(self, world, cur_room):
        self.world = world
        self.cur_room = cur_room

    def _change_room_status(self):
        pass

    def check_cur_room(self):
        if self.world.rooms[self.cur_room].who_in.name == 'wumpus':
            pass
        elif self.world.rooms[self.cur_room].who_in.name == 'bat':
            pass
        elif self.world.rooms[self.cur_room].who_in.name == 'pit':
            pass
        else:
            # print('fuh, proneslo\n')
            pass

    def check_next_rooms(self):
        next_rooms = self.world.rooms[self.cur_room].ways_to
        for room in next_rooms:
            if self.world.rooms[room].special == 'smell':
                print('hmm, wumpus is nearby\n')
            elif self.world.rooms[room].special == 'noise':
                print('I AM BATMAN\n')
            elif self.world.rooms[room].special == 'wind':
                print('look under ur feet\n')

    def process_action(self):
        try:
            action = input('Attack [A]?\n'
                           'Move [M]?\n').lower()
            if action == 'a':
                print('attack motherfucker!\n')
            elif action == 'm':
                print('ok, go to X from Y\n')
            else:
                print('kajetsya ti ne ponyal pravila\n')
                self.process_action()
        except KeyboardInterrupt:
            print('nu poka\n')
            exit(0)
        except:
            exit(0)


class Game:
    def __init__(self):
        self.prepare_game()

    def _print_rules(self):
        pass

    def _choose_difficulty(self):
        ok_status = ['easy', 'medium', 'hell']
        try:
            diff = input('Please, choose difficulty\n'
                         'Easy - standard game settings\n'
                         'Medium - more fear and horror\n'
                         'HELL - ...\n'
                         'Or you caught quit - just type "q"\n'
                         'Or remember rules - "h/help"\n').lower()
            if diff in ok_status:
                return diff
            elif diff == 'h' or diff == 'help':
                self._print_rules()
                self._choose_difficulty()
            elif diff == 'q':
                print('Nu poka :(\n')
                exit(0)
            else:
                raise ValueError
        except KeyboardInterrupt:
            print('Nu poka :(\n')
            exit(0)
        except ValueError:
            print('Try again, dude\n')
            self._choose_difficulty()

    def prepare_game(self):
        self._print_rules()
        difficulty = self._choose_difficulty()
        if difficulty == 'easy':
            world = EasyWorld(20, 3)
        elif difficulty == 'medium':
            world = MediumWorld(20, 3)
        elif difficulty == 'hell':
            world = HellWorld(20, 3)
        else:
            world = EasyWorld(20, 3)
        # TODO print start
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
                exit(0)
            except EndGame:
                print('oooooops')
                break
