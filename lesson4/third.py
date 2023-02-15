class Table:

    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

class KitchenTable(Table):

    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p

t4 = KitchenTable(1.5, 2, 0.75, 6)
