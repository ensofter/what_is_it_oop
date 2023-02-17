class T1:
    def __init__(self):
        self.n = 10

    def total(self, a):
        return self.n + int(a)

class T2:
    def __init__(self):
        self.string = 'Hi'

    def total(self, a):
        return len(self.string + str(a))


t1 = T1()
t2 = T2()

print(t1.total(35))
print(t2.total(35))
