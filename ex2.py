class Animal:

    def make_sound(self):
        pass

    # publick method
    def animal_say(self):
        print('this animal say')

    # protected method
    def _secret_method(self):
        print('thsssss this is a big secret')

    # privite method
    def __privite_method(self):
        print('this is privite method')

class Cat(Animal):

    def make_sound(self):
        self.animal_say()
        self._secret_method()

    def _secret_method(self):
        print('MEOW')

class Dog(Animal):

    def make_sound(self):
        self.animal_say()
        self._secret_method()

    def _secret_method(self):
        print('WOOF!')

if __name__ == '__main__':
    c: Cat  = Cat()
    d: Dog = Dog()
    l: list[Animal] = [c, d]
    for animal in l:
        animal.make_sound()
