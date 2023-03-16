from abc import ABC, abstractmethod


class IEngin(ABC):
    @abstractmethod
    def release_engin(self):
        pass


class JapanEngin(IEngin):
    def release_engin(self):
        print("Release Japan Engin")


class RussianEngin(IEngin):
    def release_engin(self):
        print("Release Russian Engin")


class ICar(ABC):
    @abstractmethod
    def release_car(self, engin: IEngin):
        pass


class JapaneseCar(ICar):

    def release_car(self, engin: IEngin):
        print("Собрали японский автомобиль", end='')
        engin.release_engin()


class RussianCar(ICar):
    def release_car(self, engin: IEngin):
        print("Собрали российский автомобиль", end='')
        engin.release_engin()


class IFactory(ABC):
    @abstractmethod
    def create_engin(self) -> IEngin:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class JapaneseFactory(IFactory):

    def create_engin(self) -> IEngin:
        return JapanEngin()

    def create_car(self) -> ICar:
        return JapaneseCar()


class RussianFactory(IFactory):

    def create_engin(self) -> IEngin:
        return RussianEngin()

    def create_car(self) -> ICar:
        return RussianCar()


if __name__ == '__main__':
    russia_engin = RussianFactory().create_engin()
    russia_car = RussianFactory().create_car().release_car(russia_engin)

    japanese_factory = JapaneseFactory()
    japanese_engin = japanese_factory.create_engin()
    japanese_car = japanese_factory.create_car()
    japanese_car.release_car(japanese_engin)