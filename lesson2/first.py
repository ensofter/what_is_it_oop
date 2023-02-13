class B:
    n = 5
    def adder(self, v):
        return v + self.n

w = B()

print(w.__dict__)

w.n = 8

print(w.__dict__)
