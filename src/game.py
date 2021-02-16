from src.world.world import EasyWorld
from src.world.world import MediumWorld
from src.world.world import HellWorld


class GameLogic:
    def __init__(self, world, cur_room):
        self.world = world
        self.cur_room = cur_room

    def check_cur_room(self):
        pass

    @staticmethod
    def check_next_rooms(next_rooms):
        for room in next_rooms:
            if room.special == 'smell':
                pass
            elif room.special == 'moise':
                pass
            elif room.special == 'wind':
                pass


class Game:
    def __init__(self):
        self.prepare_game()

    @staticmethod
    def _choose_difficulty():
        ok_status = ['easy', 'medium', 'hell']
        try:
            diff = input('Please, choose difficulty\n'
                         'Easy - standard game settings\n'
                         'Medium - more fear and horror\n'
                         'HELL - ...\n').lower()
            if diff in ok_status:
                return diff
            else:
                raise ValueError
        except:
            print('Try again, dude\n')

    def prepare_game(self):
        # TODO print pravila
        difficulty = self._choose_difficulty()
        # TODO print start
        if difficulty == 'easy':
            world = EasyWorld(20, 3)
        elif difficulty == 'medium':
            world = MediumWorld(20, 3)
        else:
            world = HellWorld(20, 3)
        world.gen_units()
        world.gen_map()
        start_room = world.fill_map()
        self.game_logic = GameLogic(world, start_room)

    def run(self):
        while True:
            try:
                pass
            except KeyboardInterrupt:
                exit(0)
