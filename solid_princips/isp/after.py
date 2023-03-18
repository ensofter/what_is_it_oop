from abc import ABC, abstractmethod


class ISwimmer(ABC):

    @abstractmethod
    def swim(self):
        pass


class IWalker(ABC):

    @abstractmethod
    def walk(self):
        pass


class ITalker(ABC):

    @abstractmethod
    def talk(self):
        pass


class Human(ISwimmer, IWalker, ITalker):
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        print(f'im human {self.name} and i can walk')

    def talk(self):
        print(f'im human {self.name} and i can talk')

    def swim(self):
        print(f'im human {self.name} and i can swim')


class Fish(ISwimmer):
    def __init__(self, name: str):
        self.name = name

    def swim(self):
        print(f'im fish {self.name} and i can swim')


class Cat(ISwimmer, IWalker):
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        print(f'im cat {self.name} and i can walk')

    def swim(self):
        print(f'im cat {self.name} and i can swim')


if __name__ == '__main__':
    maggy = Cat('Maggys')
    maggy.swim()




