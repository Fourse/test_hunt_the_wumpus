import random
import subprocess

from src.world.world import EasyWorld
from src.world.world import MediumWorld
from src.world.world import HellWorld

from src.utils.text_manager import TextManager
from src.utils.exceptions import EndGame
from src.utils.exceptions import WumpusDead


def quit_game():
    print(TextManager.quit())
    exit(0)


class GameLogic:
    def __init__(self, world, cur_room):
        self.world = world
        self.cur_room = cur_room

    def _moving_between_rooms(self, _to, _from, who_in):
        self.world.fill_room(
            _to,
            'occupied',
            who_in,
            who_in.special
        )
        self.world.fill_room(
            _from,
            "empty",
            None,
            None
        )

    def check_cur_room(self):
        current_room = self.world.rooms[self.cur_room]
        try:
            if current_room.who_in.name == 'wumpus':
                current_room.who_in.attack()
            elif current_room.who_in.name == 'bat':
                current_room.who_in.move()
                empty_rooms = self.world.get_empty_rooms()
                self._moving_between_rooms(
                    random.choice(empty_rooms),
                    current_room.number,
                    current_room.who_in
                )
                self.cur_room = random.choice(list(self.world.rooms.keys()))
                self.check_cur_room()
            elif current_room.who_in.name == 'pit':
                current_room.who_in.attack()
        except AttributeError:
            pass

    def attack_wumpus(self, room_number):
        try:
            if self.world.rooms[room_number].who_in.name == 'wumpus':
                self.world.rooms[room_number].who_in.alive = False
                print(TextManager.won_the_game())
                raise WumpusDead
            else:
                # TODO unsleep wumpus and pust` gulyaet
                pass
        except AttributeError:
            pass

    def check_next_rooms(self):
        next_rooms = self.world.rooms[self.cur_room].ways_to
        for room in next_rooms:
            self.world.rooms[room].process_special()

    def process_action(self):
        try:
            print(TextManager.where_i_am(self.cur_room, self.world.rooms[self.cur_room].ways_to))
            action = input(TextManager.await_action()).lower()
            current_room = self.world.rooms[self.cur_room]
            if action == 'a':
                inp = int(input(TextManager.where_you_shooting()))
                self.attack_wumpus(inp)
                current_room.who_in.attack()
            elif action == 'm':
                current_room.who_in.move()
                inp = int(input(TextManager.where_you_go()))
                self.cur_room = inp
                self.check_cur_room()
                self._moving_between_rooms(
                    self.cur_room,
                    current_room.number,
                    current_room.who_in
                )
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
            world = EasyWorld()
        elif difficulty == 'medium':
            world = MediumWorld()
        elif difficulty == 'hell':
            world = HellWorld()
        else:
            world = EasyWorld()
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
                subprocess.call("clear")
                self.game_logic.check_next_rooms()
                self.game_logic.process_action()
            except KeyboardInterrupt:
                quit_game()
            except EndGame:
                print('oooooops')
                break
            except WumpusDead:
                print('HELL YEAH')
                break
