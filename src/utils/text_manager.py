class TextManager:
    @staticmethod
    def game_rules():
        pass

    @staticmethod
    def choose_difficulty():
        return 'Please, choose difficulty\n' \
               'Easy - standard game set`tings\n' \
               'Medium - more fear and horror\n' \
               'HELL - ...\n' \
               'Or you caught quit - just type "q"\n' \
               'Or remember rules - "h/help"\n'

    @staticmethod
    def await_action():
        return 'Attack [A]?\n' \
               'Move [M]?\n'

    @staticmethod
    def quit():
        return 'Nu poka :(\n'

    @staticmethod
    def give_try():
        return 'Try again, dude\n'

    @staticmethod
    def start_game():
        return 'Nu, s bogom'

    @staticmethod
    def you_has_been_killed():
        return 'You has been killed by Wumpus :('

    @staticmethod
    def you_fell_down():
        return 'You fell down :('

    @staticmethod
    def player_moves():
        return 'Moving...'

    @staticmethod
    def player_attacks():
        return 'If only the bull`s-eye'

    @staticmethod
    def where_you_go():
        return 'Where you go?\n'

    @staticmethod
    def fly_with_bat():
        return 'I believe I can fly!'
