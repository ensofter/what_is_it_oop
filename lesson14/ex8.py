from abc import ABC, abstractmethod


class IProcessor(ABC):

    @abstractmethod
    def process(self):
        pass


class Transmitter(IProcessor):
    def __init__(self, data: str):
        self.__data = data

    def process(self):
        print(f'Данные {self.__data} переданны по каналу связи')


class Shell(IProcessor):
    def __init__(self, pc: IProcessor):
        self._processor = pc

    @abstractmethod
    def process(self):
        self._processor.process()


class HammingCoder(Shell):
    def __init__(self, pc: IProcessor):
        super().__init__(pc)

    def process(self):
        print('Наложен помехоустойчивый код Хэмминга', end='')
        self._processor.process()


class Encryptor(Shell):
    def __init__(self, pc: IProcessor):
        super().__init__(pc)

    def process(self):
        print("Шифрование данных", end='')
        self._processor.process()


if __name__ == '__main__':
    transmitter: IProcessor = Transmitter('1234')
    transmitter.process()
    print()
    hamming_coder: Shell = HammingCoder(transmitter)
    hamming_coder.process()
    print()
    encrypt: Shell = Encryptor(hamming_coder)
    encrypt.process()