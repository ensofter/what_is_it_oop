class B:
    count = 0

    def __init__(self):
        B.count += 1

    def __del__(self):
        B.count -= 1

a = B()
b = B()

print(B.count)

del a
print(B.count)

class C:
    __count = 0

    def __init__(self):
        C.__count += 1

    def __del__(self):
        C.__count -= 1

a = C()
print(C._C__count)
