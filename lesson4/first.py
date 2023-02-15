class Table:

    def __init__(self, l, w, h):

        self.length = l
        self.width = w
        self.height = h

class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = Table(1.5, 1.9, 0.75)
t2 = DeskTable(0.8, 0.8, 0.7)

print(t2.square())
