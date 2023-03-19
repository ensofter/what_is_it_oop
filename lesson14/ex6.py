from abc import ABC, abstractmethod


class IScale(ABC):
    @abstractmethod
    def weight(self) -> float:
        pass


class RussianScales(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    @property
    def weight(self) -> float:
        return self.__current_weight


class BritishScales(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    @property
    def weight(self) -> float:
        return self.__current_weight


class AdapterForBritishScales(IScale):
    def __init__(self, british_scales: BritishScales):
        self.__british_scales = british_scales

    def weight(self) -> float:
        return self.__british_scales.weight * .453


if __name__ == '__main__':
    kg: float = 55. # кг
    lb: float = 55. # фунтов

    r_scales = RussianScales(kg)
    b_scales = AdapterForBritishScales(BritishScales(lb))

    print(r_scales.weight)
    print(b_scales.weight())


