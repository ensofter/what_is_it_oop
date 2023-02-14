class Person:

    def set_name(self, name, sername):
        self.name = name
        self.sername = sername


a = Person()
a.set_name('Alex', 'Shmalex')
print(a.__dict__)
print(a.name)
print(a.sername)

class Person1:
    def __init__(self, name, sername):
        self.name = name
        self.sername = sername

b = Person1(name='Poopa', sername='Loopa')
print(b.name, b.sername)
print(b.__dict__)

class Rectangle:

    def __init__(self, width=0.5, height=2):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(width=10)
rec5 = Rectangle(height=5)

print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec5.square())
