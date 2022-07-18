import random

class Unit:
    def __init__(self, name, health=100, power=1, dexterity=1, intelligence=1):
        self.name = name
        self.health = health
        self.power = power
        self.dexterity = dexterity
        self.intelligence = intelligence

    def get_level_up(self):
        raise NotImplementedError

    def health_increase(self):
        self.health += round(random.randint(1, 20) * self.health / 100)
        if self.health > 100:
            self.health = 100
        else:
            return self.health
        return self.health

    def health_decrease(self):
        self.health -= round(random.randint(1, 20) * self.health / 100)
        if self.health < 0:
            self.health = 0
        else:
            return self.health
        return self.health

    def __str__(self):
        return f'({self.name=}, {self.health=}, {self.power=}, {self.dexterity=}, {self.intelligence=})'


class Mage(Unit):
    def __init__(
            self,
            name,
            health=100,
            power=1,
            dexterity=1,
            intelligence=1,
            type_of_magic=random.choice(['air', 'water', 'fire'])
    ):
        super().__init__(name, health=health, power=power, dexterity=dexterity, intelligence=intelligence)
        self.type_of_magic = type_of_magic

    def get_level_up(self):
        self.intelligence += int(self.intelligence < 10)
        # якщо вираз в дужках Істина, то додає 1, якщо Брехня, то 0
        return self. intelligence

    def __str__(self):
        str_unit = super().__str__()
        return f'{str_unit}, {self.type_of_magic=}'


class Archer(Unit):
    def __init__(
            self,
            name,
            health=100,
            power=1,
            dexterity=1,
            intelligence=1,
            type_of_bow=random.choice(['bow', 'crossbow', 'sling'])
    ):
        super().__init__(name, health=health, power=power, dexterity=dexterity, intelligence=intelligence)
        self.type_of_bow = type_of_bow

    def get_level_up(self):
        self.dexterity += int(self.dexterity < 10)
        return self.dexterity

    def __str__(self):
        str_unit = super().__str__()
        return f'{str_unit}, {self.type_of_bow=}'


class Knight(Unit):
    def __init__(
            self,
            name,
            health=100,
            power=1,
            dexterity=1,
            intelligence=1,
            type_of_weapon=random.choice(['sword', 'axe', 'peak'])
    ):
        super().__init__(name, health=health, power=power, dexterity=dexterity, intelligence=intelligence)
        self.type_of_weapon = type_of_weapon

    def get_level_up(self):
        self.power += int(self.power < 10)
        return self.power

    def __str__(self):
        str_unit = super().__str__()
        return f'{str_unit}, {self.type_of_weapon=}'

n = 10
mage = Mage('Gnourus')
for _ in range(random.randint(1, n)):
    mage.get_level_up()
for _ in range(random.randint(1, n)):
    mage.health_decrease()
for _ in range(random.randint(1, n)):
    mage.health_increase()
print(mage)

archer = Archer('Dimitrus')
for _ in range(random.randint(1, n)):
    archer.get_level_up()
for _ in range(random.randint(1, n)):
    archer.health_decrease()
for _ in range(random.randint(1, n)):
    archer.health_increase()
print(archer)

knight = Knight('Arthur')
for _ in range(random.randint(1, n)):
    knight.get_level_up()
for _ in range(random.randint(1, n)):
    knight.health_decrease()
for _ in range(random.randint(1, n)):
    knight.health_increase()
print(knight)
