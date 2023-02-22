class Triangle:

    def __init__(self, a=0, b=0, c=0):
        self.__a = a
        self.__b = b
        self.__c = c

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    def set_c(self, c):
        self.__c = c

    def get_c(self):
        return self.__c

abc = Triangle()
print(abc.get_a())
print(abc.get_b())
print(abc.get_c())

abc.set_a(10)
print(abc.get_a())
abc.set_b(15)
print(abc.get_b())
abc.set_c(20)
print(abc.get_c())
