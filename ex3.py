from functools import singledispatch


class Animal(object):

    @singledispatch
    def my_method(arg):
        print("INT")
        print(arg)

    @my_method.register(str)
    def _(arg):
        print("STR")
        print(arg)

if __name__ == '__main__':
    Animal.my_method(1)
    Animal.my_method('a')
