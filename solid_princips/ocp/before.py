# open-closed
# открытый закрытый принцип. Классы можно расширять, но желательно на прямую не модифицировать
import sys
import time


class Logger:
    def log(self, message: str):
        current_time = time.localtime()
        sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


if __name__ == '__main__':
    logger = Logger()
    logger.log('An error has happened!')
