class Pokemon:

    def type(self):
        return ['Grass', 'Poison']

class Bulbasaur(Pokemon):
    level = 1

    def __init__(self):
        self.hp = 3
        self.attack = 3
        self.defense = 3
        self.speed = 3
        self.height = 0.7
        self.weight = 6.9

class Ivysaur(Pokemon):
    level = 16

    def __init__(self):
        self.hp = 4
        self.attack = 4
        self.defense = 4
        self.speed = 4
        self.height = 1
        self.weight = 13

class Venusaur(Pokemon):
    level = 32

    def __init__(self):
        self.hp = 5
        self.attack = 5
        self.defense = 5
        self.speed = 5
        self.height = 5
        self.weight = 100

print(Pokemon.type(Ivysaur))