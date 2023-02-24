from math import pi


class Cylinder:
    __initialized = False

    def __init__(self, di:int=0, h:int=0):
        self.di = di
        self.h = h
        self.area = self.make_area(di, h)
        self.__initialized = True

    def __setattr__(self, attr, value):
        if self.__initialized:
            match attr:
                case 'di':
                    self.__dict__[attr] = value
                    self.__dict__['area'] = self.make_area(self.di, self.h)
                case 'h':
                    self.__dict__[attr] = value
                    self.__dict__['area'] = self.make_area(self.di, self.h)
                case 'area':
                    print('can\'t set this attribute value')
        else:
            object.__setattr__(self, attr, value)

    @staticmethod
    def make_area(di, hi):
        circle = pi * di ** 2/4
        side = pi * di * hi
        return round(circle * 2 + side, 2)


a = Cylinder(1, 2)
print(a.area)
a.h = 3
print(a.area)
a.di = 3
print(a.area)
print(a.make_area(2, 2))
a.area = 15
