from abc import ABC, abstractmethod


class Phone:
    def __init__(self):
        self.data: str = ''

    def about_phone(self) -> str:
        return self.data

    def append_data(self, string: str):
        self.data += string


class IDeveloper(ABC):
    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def system_install(self):
        pass

    @abstractmethod
    def get_phone(self) -> Phone:
        pass


class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data("Произведен дисплей Samsung;\n")

    def create_box(self):
        self.__phone.append_data("Произведен корпус Samsung;\n")

    def system_install(self):
        self.__phone.append_data("Установлена система Android;\n")

    def get_phone(self) -> Phone:
        return self.__phone


class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data("Произведен дисплей Iphone;\n")

    def create_box(self):
        self.__phone.append_data("Произведен корпус Iphone;\n")

    def system_install(self):
        self.__phone.append_data("Установлена система Ios;\n")

    def get_phone(self) -> Phone:
        return self.__phone


class Director:

    def __init__(self, developer: IDeveloper):
        self.__developer = developer

    def set_developer(self, developer: IDeveloper):
        self.__developer = developer

    def create_only_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        return self.__developer.get_phone()

    def create_full_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.system_install()
        return self.__developer.get_phone()


if __name__ == '__main__':
    android_developer: IDeveloper = AndroidDeveloper()
    android_director = Director(android_developer)
    samsung_full_phone: Phone = android_director.create_full_phone()
    print(samsung_full_phone.about_phone())

    iphone_developer: IDeveloper = IphoneDeveloper()
    iphone_director = Director(iphone_developer)
    iphone: Phone = iphone_director.create_only_phone()
    print(iphone.about_phone())