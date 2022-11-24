import random
from pack import Pack


START_MONEY = 10

class Shop:
    def __init__(self, pack: Pack, current_round=1,
            add_attack=0, add_health=0, add_money=0):
        self.pack = pack
        self.current_round = current_round

        self.pets = []
        self.foods = []

        self.money = -1
        self.add_attack = add_attack
        self.add_health = add_health
        self.add_money = add_money
        self._pets_pool = []
        self._foods_pool = []
        self._num_pets = -1
        self._num_foods = -1
        self._pool_set = False

        self.setup_turn()

    def setup_turn(self):
        self.set_pool()
        self.roll_shop()
        self.money = START_MONEY + self.add_money

    def set_pool(self):
        # set number of pets and foods
        if self.current_round < 5:
            self._num_pets = 3
            self._num_foods = 2
        elif 5 <= self.current_round < 9:
            self._num_pets = 4
            self._num_foods = 2
        else:
            self._num_pets = 5
            self._num_foods = 2
        
        # set pool for pets and foods
        max_tier = (self.current_round - 1) // 2 + 1
        self._pets_pool = [p.copy() for p in self.pack.pets if p.tier <= max_tier]
        self._foods_pool = [f.copy() for f in self.pack.foods if f.tier <= max_tier]

        self._pool_set = True

    def roll_shop(self, free: bool=False):
        self.pets = random.choices(self._pets_pool, k=self._num_pets)
        self.foods = random.choices(self._foods_pool, k=self._num_foods)

        if not free:
            self.money -= 1

    def __str__(self) -> str:
        return f'{self.pets}, {self.foods}'
        
    def __repr__(self) -> str:
        return self.__str__()
