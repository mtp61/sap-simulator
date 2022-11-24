from pet import Pet


class Team:
    def __init__(self, team: list[Pet]=[None, None, None, None, None]):
        self.team = team

    def __str__(self) -> str:
        return str(self.team)
    
    def __repr__(self) -> str:
        return self.__str__()
