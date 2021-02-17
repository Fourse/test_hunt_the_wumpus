import subprocess


class Display:
    def __init__(self):
        self.data = []
        self.msg = ""
        self.start_game()

    def help_menu(self):
        pass

    def rules(self):
        self.data = [
            f'{"-" * 59}',
            f'{" " * 21}HUNT THE WUMPUS{" " * 22}',
            f'{"-" * 59}',
            'The Wumpus lives in cave of 20 rooms.',
            'Each room has 3 tunnels leading to other rooms.',
            'Hazards:',
            'Bottomless pits - two rooms have bottomless pits in them.',
            'If you go there, you fall into the pit and lose.',
            'Super bats - two other rooms have super bats.',
            'If you go there,',
            'a bat grabs you and takes you to some other room at random',
            '(Which may be troublesome).',
            'You should kill Wumpus, but you have only 5 arrows...',
            'Good luck!',
            f'{"-" * 59}',
            'Press Enter if you ready: '
        ]

    def start_game(self):
        self.rules()
        while self.await_input() != "":
            self.msg = ""
            pass
        self.clear_msg()

    @staticmethod
    def clear():
        subprocess.call("clear")

    def create_msg(self):
        for data in self.data:
            text_len = len(data)
            spaces = 1
            self.msg += f'|{" " * 1}{data}{" " * (60 - (text_len + spaces))}|\n'

    def render_display(self):
        self.clear()
        self.create_msg()

    def await_input(self):
        self.render_display()
        user_input = input(self.msg)
        if user_input == 'qq':
            raise KeyboardInterrupt
        self.clear_msg()
        return user_input

    def clear_msg(self):
        self.data.clear()
        self.data = [
            f'{"-" * 59}',
            f'{" " * 21}HUNT THE WUMPUS{" " * 22}',
            f'{"-" * 59}',
            f'         [qq] - quit   [a] - attack   [m] - move',
            f'{"-" * 59}',
        ]
        self.msg = ""

    def add_data(self, data):
        self.data.append(data)

    def change_last_data(self, data):
        self.data[-1] = data
