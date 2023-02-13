import random

class Warior:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def hit(self, enemy):
        print(f'{enemy.name} атаковал {self.name}')
        self.health -= 20
        print(f'уровень здоровья {self.name} = {self.health}')


poopa = Warior(name = 'poopa', health = 100)
loopa = Warior(name = 'loopa', health = 100)

wariors = [poopa, loopa]

while True:
    random.shuffle(wariors)
    wariors[0].hit(wariors[1])
    if poopa.health == 0:
        print('poopa is died')
        break
    elif loopa.health == 0:
        print('loopa is died')
        break
