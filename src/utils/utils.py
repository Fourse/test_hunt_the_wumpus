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
