

class Rectangle:

    def __init__(self, w, h):
        self._w = w
        self._h = h

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, value):
        self._w = value

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, value):
        self._h = value

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'

    @property
    def area(self):
        return self.height * self.width


class Square(Rectangle):

    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._h = self._w = value

    @Rectangle.height.setter
    def height(self, value):
        self._h = self._w = value


def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'expected: {expected}, got {rc.area}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    square = Square(5)
    print(square)
    print(square.area)

    use_it(square)
