class MyCustomMethod:

    def __init__(self, sign):
        self.sign = sign

    def __add__(self, other):
        s = self.sign + str(other)
        return s

t1 = MyCustomMethod('!!!')
r = t1 + 666
print(r)
