


def decor(func):
    def wrapper():
        print('!!! Before')
        func()
        print('!!! After')
    return wrapper


@decor
def my_func():
    print('This is my func')

my_func()
