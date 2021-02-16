class EndGame(Exception):
    pass


class WonGame(EndGame):
    pass


class LostGame(EndGame):
    print('Better luck next time')
