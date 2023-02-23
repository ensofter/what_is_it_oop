class Room:

    class WinDoor:
        def __init__(self, w, h):
            self.width = w
            self.height = h

        def square(self):
            return self.width * self.height

    class Wallpapper:
        def __init__(self, w, h):
            self.width = w
            self.height = h

        def square(self):
            return self.width * self.height

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.wd = []

    def square(self):
        return 2 * self.z * (self.x + self.y)

    def add_wd(self, w, h):
        self.wd.append(Room.WinDoor(w, h))

    def work_surface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square()
        return new_square

    def wallpapper_qty(self, w, h):
        surface_square = self.work_surface()
        wallpapper_square = w * h
        return surface_square // wallpapper_square

r1 = Room(6, 3, 2.7)
print(r1.square())
r1.add_wd(1, 1)
r1.add_wd(1, 1)
r1.add_wd(1, 2)

print(r1.work_surface())
print(r1.wallpapper_qty(1, 2))
