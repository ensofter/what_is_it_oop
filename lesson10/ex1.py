class A:

    def __init__(self, qty):
        self.qty = qty

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.qty -= 1
            return '+'
        else:
            raise StopIteration

a = A(4)
for i in a:
    print(i)
