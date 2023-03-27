from typing import List
from typing import Dict


class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, pasport: str):
        self.__name = name
        self.__pasport = pasport

    @property
    def name(self):
        return self.__name

    @property
    def pasport(self):
        return self.__pasport


class FlyWeight:
    def __init__(self, shared: Shared):
        self.__shared = shared


    def process(self, unique: Unique):
        print(f'Отображаем общие данные: {self.__shared.company}, {self.__shared.position}'
              f'и уникальныеЖ {unique.name}, {unique.pasport}')

    def get_data(self) -> str:
        return self.__shared.company + '_' + self.__shared.position


class FlyWeightFactory:

    def get_key(self, shred: Shared):
        return f'{shred.company}_{shred.position}'

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, FlyWeight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = FlyWeight(shared)

    def get_flyweight(self, shared: Shared):
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print(f'Фабрика легковесов: общий объект по ключу {key} не найден. Создаем новый')
            self.__flyweights[key] = FlyWeight(shared)
        else:
            print(f'Фабрика легковесов: Извлекаем данные из имеющихся записей по ключу {key}')
        return self.__flyweights[key]

    def list_flyweight(self):
        count: int = len(self.__flyweights)
        print(f'\nФабрика легковесов: Всего {count} записей')


def add_specialist_database(ff: FlyWeightFactory, company: str, position: str, name: str, pasport: str):
    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, pasport))


if __name__ == '__main__':
    shared_list: List[Shared] = \
        (Shared('Microsoft', 'управляющий'),
         Shared('Google', 'андройд разработчик'),
         Shared('Google', 'веб разработчик'),
         Shared('Apple', 'айос разработчик'))

    factory = FlyWeightFactory(shared_list)
    factory.list_flyweight()

    add_specialist_database(factory, "Google", "веб разработчик", "Борис", "1м-456743")
    add_specialist_database(factory, "Ozon", "тестировщик", "Алексей", "zz-1488")

    factory.list_flyweight()