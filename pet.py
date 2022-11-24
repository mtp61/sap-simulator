

class Pet:
    def __init__(self, name, tier, attack, health, ability=None, xp=0):
        self.name = name
        self.tier = tier
        self.attack = attack
        self.health = health
        self.ability = ability
        self.xp = xp

    def copy(self):
        return Pet(self.name, self.tier, self.attack, self.health,
                self.ability, self.xp)

    def __str__(self):
        return f'({self.name} {self.attack}-{self.health} {self.xp})'

    def __repr__(self):
        return self.__str__()
