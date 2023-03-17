import sys
import time


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message: str):
        sys.stderr.write(f"{self.prefix} --> {message}\n")


class CustomLogger(Logger):
    def __init__(self):
        super().__init__()
        self.prefix = time.strftime('%Y-%b-%d', time.localtime())


if __name__ == '__main__':
    logger = Logger()
    logger.log('An error has happened!')

    c_logger = CustomLogger()
    c_logger.log('An error has happened!')