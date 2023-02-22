class Double:

    def __init__(self, l):
        self.double = Double.__make_double(l)

    def __make_double(old):
        new = []
        for i in old:
            new.append(i)
            new.append(i)
        return new

nums = Double([1, 6, 12])
print(nums.double)
print(nums.__make_double([1, 2]))
