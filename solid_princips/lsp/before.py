class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):
        print('eat some food!')


class Cat(Animal):
    def eat(self, amount: float = 0.1):
        if amount > 0.3:
            print('cant eat that much!')
        else:
            print('Ate some cat food!')


class Dog(Animal):
    def eat(self):
        print('Ate some dof food!')


if __name__ == '__main__':
    pluto = Dog({'name': 'Pluto', 'age': 3})
    rem = Dog({'name': 'Rem', 'age': 2})
    buttons = Cat(('Meggy', 10))

    animals = (pluto, rem)
    for animal in animals:
        if animal.attributes['age'] > 2:
            print(animal.attributes['name'])