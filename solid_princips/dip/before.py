import sys
import time


class TerminalPrinter:
    def write(self, msg: str):
        sys.stderr.write(f'{msg}\n')


class FilePrinter:
    def write(self, msg: str):
        with open('output.txt', 'a+', encoding='UTF8') as f:
            f.write(f'{msg}\n')


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log_stderr(self, message):
        terminal = TerminalPrinter()
        terminal.write(f'{self.prefix} --> {message}')

    def log_file(self, message):
        file = FilePrinter()
        file.write(f'{self.prefix} --> {message}')
