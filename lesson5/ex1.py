class T1:
    def __init__(self):
        self.n = 10

    def total(self, a):
        return self.n + int(a)

class T2:
    def __init__(self):
        self.string = 'Hi'

    def total(self, a):
        return len(self.string + str(a))


t1 = T1()
t2 = T2()

print(t1.total(35))
print(t2.total(35))


class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __str__(self):
        s = f'{self.field1} and {self.field2}'
        return s


a = A(3, 4)
b = str(a)
print(a)
print(b)


class Rectangle:
    def __init__(self, w, h, sign):
        self.w = int(w)
        self.h = int(h)
        self.sign = str(sign)

    def __str__(self):
        rect = []
        # кол-во строк
        for i in range(self.h):
            # знак повторяется w раз
            rect.append(self.sign * self.w)
        # превращаем список в строку
        rect = '\n'.join(rect)
        return rect

b = Rectangle(10, 3, '*')
print(b)
