# interface segregation principle
# клиент не должен зависеть от всех методов которые есть у класса и не должен их подключать себе.


class Creature:

    def walk(self):
        pass

    def talk(self):
        pass

    def swim(self):
        pass


class Human(Creature):
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        print(f'im human {self.name} and i can walk')

    def talk(self):
        print(f'im human {self.name} and i can talk')

    def swim(self):
        print(f'im human {self.name} and i can swim')


class Fish(Creature):
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f'im fish {self.name} and i can swim')


class Cat(Creature):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'im cat {self.name} and i can walk')

    def swim(self):
        print(f'im cat {self.name} and i can swim')


if __name__ == '__main__':
    maggy = Cat('Maggy')
    maggy.walk()