import sys
import time
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def write(self, msg: str):
        pass


class TerminalPrinter(Printer):
    def write(self, msg: str):
        sys.stderr.write(f'{msg}\n')


class FilePrinter(Printer):
    def write(self, msg: str):
        with open('output.txt', 'a+', encoding='UTF8') as f:
            f.write(f'{msg}\n')


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message: str, printer: Printer):
        printer.write(message)


if __name__ == '__main__':
    printer = TerminalPrinter()
    log = Logger()
    log.log("Wow message!!!", printer)
