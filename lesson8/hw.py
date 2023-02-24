class Snow:

    def __init__(self, qty: int = 0):
        self.__qty = qty

    def __add__(self, n: int):
        return Snow(self.__qty + n)

    def __sub__(self, n: int):
        return Snow(self.__qty - n)

    def __mul__(self, n: int):
        return Snow(self.__qty * n)

    def __truediv__(self, n: int):
        return Snow(int(self.__qty / n))

    def make_snow(self, n: int):
        snows = ''
        for i in range(self.__qty):
            snows += '*' * n + '\n'
        return snows

    def __call__(self, n):
        self.__qty = n


s = Snow(3)
print(s.make_snow(13))
s1 = s + 3
print(s1.make_snow(4))


