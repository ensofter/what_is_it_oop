


def decor(func):
    def wrapper(*args, **kwargs):
        print('!!! Before')
        func(*args, **kwargs)
        print('!!! After')
    return wrapper


@decor
def my_func(p1, p2):
    print('This is my func')
    print(p1)
    print(p2)

@decor
def my_func_1(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

if __name__ == '__main__':
    my_func(1, 2)
    my_func_1(1, 2, 3)
