class Animal:
    def __init__(self, name: str, age: int):
        self.attributes = dict(name=name, age=age)

    def eat(self, _amount: float = None):
        print('eat some food!')


class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def eat(self, amount: float = 0.1):
        if amount > 0.3:
            print('cant eat that much!')
        else:
            print('Ate some cat food!')


class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def eat(self, _amount: float = None):
        print('Ate some dof food!')


if __name__ == '__main__':
    pluto = Dog('Pluto', 3)
    rem = Dog('Rem', 2)
    buttons = Cat('Meggy', 10)

    animals = (pluto, rem, buttons)
    for animal in animals:
        if animal.attributes['age'] > 2:
            print(animal.attributes['name'])
