class Computer:

    __cpu: str = None
    __ram: str = None
    __mouse: str = None
    __keyboard: str = None
    __monitor: str = None
    __box: str = None

    def cpu(self, cpu: str):
        self.__cpu = cpu
        return self

    def ram(self, ram: str):
        self.__ram = ram
        return self

    def mouse(self, mouse: str):
        self.__mouse = mouse
        return self

    def keyboard(self, keyboard: str):
        self.__keyboard = keyboard
        return self

    def monitor(self, monitor: str):
        self.__monitor = monitor
        return self

    def box(self, box: str):
        self.__box = box
        return self

    @staticmethod
    def builf_gaming_computer():
        return Computer().cpu('').ram('').monitor('').mouse('').box('').keyboard('')

    @staticmethod
    def build_office_computer():
        return Computer().cpu('').ram('').monitor('').mouse('').box('').keyboard('')
