

class Food:
    def __init__(self, name, tier, effect=None):
        self.name = name
        self.tier = tier
        self.effect = effect

    def copy(self):
        return Food(self.name, self.tier, self.effect)

    def __str__(self):
        return f'({self.name})'

    def __repr__(self) -> str:
        return self.__str__()
