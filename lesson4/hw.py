import random


class Npc:

    def __init__(self, n, c):
        self.uniq_number = n
        self.command = c


class Soldier(Npc):

    def follow_to_hero(self, hero):
        self.belong_to = hero


class Hero(Npc):

    def __init__(self, n, c, l=0):
        super().__init__(n, c)
        self.level = l

    def level_up(self):
        self.level += 1

human_hero = Hero(n=1, c='poopa')
human_army = []

ufo_hero = Hero(n=2, c='loopa')
ufo_army = []


for i in range(3, 23):
    soldier = Soldier(n=i, c=random.choice(['poopa', 'loopa']))
    if soldier.command == 'poopa':
        human_army.append(soldier)
        continue
    ufo_army.append(soldier)

print('human_army: ', len(human_army))
print('ufo_army: ', len(ufo_army))

if len(human_army) > len(ufo_army):
    human_hero.level_up()
else:
    ufo_hero.level_up()

print(human_hero.level)
print(ufo_hero.level)

