import copy


class Sheep:
    __name: str = ''
    __params: dict = {'Вес': 20, 'Рост': .34}

    def __init__(self, donor: 'Sheep' = None):
        if donor is not None:
            self.name = donor.name
            self.__params = copy.deepcopy(donor.params)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def params(self) -> dict:
        return self.__params

    @params.setter
    def params(self, weight: int):
        self.__params['Вес'] = weight

    def clone(self):
        return Sheep(self)


if __name__ == '__main__':
    molly = Sheep()
    molly.params = 60
    molly.name = 'Molly'

    milly_1 = molly.clone()

    print(f"original NAME: {molly.name}, original PARAMS: {molly.params}")
    print(f"clone NAME: {milly_1.name}, PARAMS: {milly_1.params}")

    milly_1.name = 'Это клон Молли'
    milly_1.params = 33

    print(f"original NAME: {molly.name}, original PARAMS: {molly.params}")
    print(f"clone NAME: {milly_1.name}, PARAMS: {milly_1.params}")