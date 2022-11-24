from team import Team
from shop import Shop
from pack import Pack


class Simulation:
    def __init__(self, pack: Pack, current_round=1, team: Team=None, shop: Shop=None):
        self.pack = pack
        self.current_round = current_round
        self.team = team if team else Team()
        self.shop = shop if shop else Shop(pack, current_round)
    
    def __str__(self) -> str:
        return f'{self.team}, {self.shop}'

    def __repr__(self) -> str:
        return self.__str__()
