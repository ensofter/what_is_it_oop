class A:
    def __init__(self, v, x):
        self.field1 = v
        self.__x = x

    def __setattr__(self, attr, value):
        match attr:
            case 'field1':
                self.__dict__[attr] = value
            case '_A__x':
                self.__dict__[attr] = value
            case _:
                raise AttributeError


a = A(10, 20)
print(a.field1)
print(a._A__x)
