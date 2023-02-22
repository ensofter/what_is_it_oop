class B:
    __count = 0

    def __init__(self):
        B.__count += 1

    def __del__(self):
        B.__count -= 1

    def qty_objects():
        return B.__count

a = B()
b = B()
print(B.qty_objects())
