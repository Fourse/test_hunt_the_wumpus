import subprocess


class Display:
    def __init__(self):
        self.start_game()
        self.game_mode = None
        self.data = []
        self.msg = ""

    def print_rules(self):
        self.clear()
        self.data = [
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
        self.create_msg()
        user_input = input(self.msg)
        if user_input == "":
            self.create_msg()
        else:
            self.print_rules()

    def start_game(self):
        self.print_rules()

    @staticmethod
    def clear():
        subprocess.call("clear")

    def create_msg(self):
        head = [
            f'|{"-" * 60}|\n',
            f'|{" " * 22}HUNT THE WUMPUS{" " * 23}|\n',
            f'|{"-" * 60}|\n',
        ]

        for data in self.data:
            text_len = len(data)
            spaces = 1
            head.append(f'|{" " * 1}{data}{" " * (60 - (text_len + spaces))}|\n')
        head.append(f'|{"-" * 60}|\n')
        head.append('\n Press Enter if you ready: ')

        self.msg = "".join(head)

    def print_msg(self):
        print(self.msg)

    def render_display(self):
        self.clear()
        self.create_msg()
        self.print_msg()
        self.clear_msg()

    def await_input(self):
        self.render_display()
        # TODO await input

    def clear_msg(self):
        self.data.clear()
        self.msg = ""

    def end_game(self, status, msg):
        self.render_display()
