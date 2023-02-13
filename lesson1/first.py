class A:
    field1 = 1

    def str_field(self):
        print(self.field1)

class B(A):
    field2 = 2

    def str_field(self):
        print(self.field1, self.field2)

class C(A):
    field3 = 3

    def str_field(self):
        print(self.field1, self.field3)
