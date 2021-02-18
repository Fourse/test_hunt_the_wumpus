import subprocess


class Display:
    def __init__(self):
        self.main_data = []
        self.footer = []
        self.msg = ""
        self.start_game()

    def help_menu(self):
        pass

    def rules(self):
        self.main_data = [
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
            'Good luck!'
        ]
        self.footer = [
            f'{"-" * 59}',
            'Press Enter if you ready: '
        ]

    def start_game(self):
        self.rules()
        while self.await_input() != "":
            self.msg = ""
            pass
        self.clear_main()
        self.clear_footer()

    @staticmethod
    def clear():
        subprocess.call("clear")

    def create_msg(self):
        for data in self.main_data:
            text_len = len(data)
            spaces = 1
            self.msg += f'|{" " * 1}{data}{" " * (60 - (text_len + spaces))}|\n'
        for foot in self.footer:
            text_len = len(foot)
            spaces = 1
            self.msg += f'|{" " * 1}{foot}{" " * (60 - (text_len + spaces))}|\n'

    def render_display(self):
        self.clear()
        self.create_msg()

    def await_input(self):
        self.render_display()
        user_input = input(self.msg)
        if user_input == 'q':
            raise KeyboardInterrupt
        self.clear_footer()
        return user_input

    def clear_footer(self):
        self.footer.clear()
        self.footer = [
            f'{"-" * 59}',
            ''
        ]
        self.msg = ""

    def clear_main(self):
        self.main_data.clear()
        self.main_data = [
            f'{"-" * 59}',
            f'{" " * 21}HUNT THE WUMPUS{" " * 22}',
            f'{"-" * 59}',
            f'{"-" * 10}[q] - quit   [a] - attack   [m] - move{"-" * 10}',
            f'{"-" * 59}',
        ]
        self.msg = ""

    def change_main_data(self, data):
        self.main_data.append(data)

    def change_footer(self, data):
        self.footer[-1] = data
        self.msg = ""
