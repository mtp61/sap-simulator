from team import Team


class Battle:
    def __init__(self, team1: Team, team2: Team, verbose: bool=False) -> None:
        self.team1 = team1
        self.team2 = team2
        self.verbose = verbose

    def __str__(self) -> str:
        return f'{self.team1} {self.team2}'

    def __repr__(self) -> str:
        return self.__str__()
