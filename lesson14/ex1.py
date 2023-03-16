from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print('Выпущен легковой автомобиль')


class Truck(IProduct):
    def release(self):
        print('Выпущен грузовой автомобиль')


class IWorkshop(ABC):
    @abstractmethod
    def create(self):
        pass


class CarWorkshop(IWorkshop):
    def create(self):
        return Car()


class TruckWorkshop(IWorkshop):
    def create(self):
        return Truck()


if __name__ == '__main__':
    creator = CarWorkshop()
    car = creator.create()


    creator = TruckWorkshop()
    truck = creator.create()

    car.release()
    truck.release()