class EndGame(Exception):
    pass


class WonGame(EndGame):
    pass


class LostGame(EndGame):
    pass


class WumpusDead(Exception):
    pass
