class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, p, l, w, h):
        Table.__init__(self, l, w, h)
        self.places = p


class KitchenTable1(Table):
    def __init__(self, l=1, w=1, h=0.7, p=4):
        Table.__init__(self, l, w, h)
        self.places = p

