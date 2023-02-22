class Full:

    def __init__(self, field):
        self.__field = field

    def set_field(self, field):
        self.__field = field

    def get_field(self):
        return self.__field

obj = Full(8)
obj.set_field(3)
print(obj.get_field())

try:
    print(obj.__field)
except AttributeError:
    print('There is no attrubute __field')

obj.__field = 5
print(obj.__field)
print(obj.get_field())
