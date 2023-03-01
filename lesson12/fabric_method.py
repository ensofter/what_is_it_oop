from abc import ABC, abstractmethod


class Cellphone(ABC):

    @abstractmethod
    def call(self) -> str:
        pass


class CellphoneCompany(ABC):

    @abstractmethod
    def make_phone(self):
        pass

    def do_call(self) -> str:
        product = self.make_phone()

        # work with product
        result = product.call()
        return result


class Apple(CellphoneCompany):

    def make_phone(self) -> Cellphone:
        return Iphone()


class Google(CellphoneCompany):

    def make_phone(self) -> Cellphone:
        return Android()


class Iphone(Cellphone):

    def call(self) -> str:
        return "this is Iphone"


class Android(Cellphone):

    def call(self) -> str:
        return "this is Android"


if __name__ == '__main__':

    google = Google().do_call()
    apple = Apple().do_call()
    print(google)
    print(apple)


