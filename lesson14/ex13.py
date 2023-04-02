from abc import ABC, abstractmethod
from typing import List, Deque


class ICommand(ABC):

    @abstractmethod
    def positive(self):
        pass

    @abstractmethod
    def negative(self):
        pass


class Conveyor:
    def on(self):
        print('Конвейер включен')

    def off(self):
        print('Конвейер выключен')

    def speed_increase(self):
        print('Увеличение скорости конвейера')

    def speed_decrease(self):
        print('Уменьшение скорости конвейера')


class ConveyorWorkCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.__conveyor: Conveyor = conveyor

    def positive(self):
        self.__conveyor.on()

    def negative(self):
        self.__conveyor.off()


class ConveyorAdjustCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.__conveyor: Conveyor = conveyor

    def positive(self):
        self.__conveyor.speed_increase()

    def negative(self):
        self.__conveyor.speed_decrease()


class Multipult:
    def __init__(self):
        self.__commands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__commands[button] = command

    def press_on(self, button: int):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


if __name__ == '__main__':
    conveyor = Conveyor()

    multipult = Multipult()
    multipult.set_command(0, ConveyorWorkCommand(conveyor))
    multipult.set_command(1, ConveyorAdjustCommand(conveyor))

    multipult.press_on(0)
    multipult.press_on(1)
    multipult.press_cancel()
    multipult.press_cancel()