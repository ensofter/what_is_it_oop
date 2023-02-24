class A:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)

class B:
    def __init__(self, *args):
        self.a_list = []
        for i in args:
            self.a_list.append(A(i))

    def __getitem__(self, i):
        return self.a_list[i]

group = B(5, 10, 'abc')
print(group.a_list[1])
print(group[1])


