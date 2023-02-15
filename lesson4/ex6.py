class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h

        if isinstance(self, KitchenTable):
            p = int(input('Сколько мест: '))
            self.places = p


class KitchenTable(Table):
    places = 4

    def set_places(self, p):
        self.places = p

t5 = KitchenTable()
print(t5.places)
