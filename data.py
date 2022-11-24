import json


PACKS_DATA_PATH = './data/packs.json'
PETS_DATA_PATH = './data/pets.json'
FOODS_DATA_PATH = './data/foods.json'


def load_pack(name: str):
    with open(PACKS_DATA_PATH, 'r') as file:
        packs = json.loads(file.read())
        if name not in packs.keys():
            raise Exception(f'Pack "{name}" not found')
        return packs[name]['pets'], packs[name]['foods']


def load_pets(pets: list[str]):
    with open(PETS_DATA_PATH, 'r') as file:
        all_pets = json.loads(file.read())
        out = []
        for name in pets: # iterate through to maintain order
            for p in all_pets:
                if p['name'] == name:
                    out.append(p)
                    break
            else:
                raise Exception(f'Pet "{name}" not found')
        return out


def load_foods(foods: list[str]):
    with open(FOODS_DATA_PATH, 'r') as file:
        all_foods = json.loads(file.read())
        out = []
        for name in foods: # iterate through to maintain order
            for f in all_foods:
                if f['name'] == name:
                    out.append(f)
                    break
            else:
                raise Exception(f'Food "{name}" not found')
        return out