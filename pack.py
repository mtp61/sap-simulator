from data import load_pack, load_pets, load_foods
from pet import Pet
from food import Food


class Pack:
    def __init__(self, name='test'):
        self.name = name
        self.pets_names, self.foods_names = load_pack(name)
        self.pets = [Pet(**p) for p in load_pets(self.pets_names)]
        self.foods = [Food(**f) for f in load_foods(self.foods_names)]
        self.pets_dict = {p.name: p for p in self.pets}
        self.foods_dict = {f.name: f for f in self.foods}


if __name__ == '__main__':
    pack = Pack()
    print(pack.pets)
    print(pack.pets[0].name)
    print(pack.pets[0].attack)
    print(pack.foods)
    print(pack.foods[0].name)
