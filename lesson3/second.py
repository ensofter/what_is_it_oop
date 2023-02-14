class Person:

    def __init__(self, n, s, c=1):
        self.name = n
        self.sername = s
        self.cvalification = c

    def get_info(self):
        print(f'{self.name}, {self.sername}, {self.cvalification}')

    def __del__(self):
        print(f'До свидания мистер {self.name} {self.sername}')

pepa = Person('Pepa', 'Poopa', 5)
loopa = Person('Loopa', 'Doopa', 6)
kvacha = Person('Kvacha', 'Bing', 3)

c = pepa.cvalification

for person in [pepa, loopa, kvacha]:
    person.get_info()
    if person.cvalification < c:
        del person
    else:
        c = person.cvalification
