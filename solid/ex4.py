from abc import ABC, abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass #реализация

    def fax(self, document):
        pass #реализация

    def scan(self, document):
        pass #реализация


class OldFashionPrinter(Machine):
    def print(self, document):
        # тут все ок, но что делать, с остальными методами?
        pass

    def fax(self, document):
        """ This method is not working here """
        raise NotImplementedError

    def scan(self, document):
        """ This method is not working here """
        raise NotImplementedError("Printer cannot scan")


# как надо

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scaner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(f"I'm printing '{document}'")


class MyFax(Fax):
    def fax(self, document):
        print(f"i'm faxing '{document}'")


class MyScanner(Scaner):
    def scan(self, document):
        print(f"i'm scanning '{document}'")

class PhotoCopier(Printer, Scaner):

    def print(self, document):
        print(f"I'm printing '{document}'")

    def scan(self, document):
        print(f"I'm scaning '{document}'")


# интерфейс для мультифункционального устройства
class MultiFunctionDevice(Printer, Scaner, Fax, ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MyMultifunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, fax, scaner):
        self.scaner = scaner
        self.fax = fax
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def fax(self, document):
        self.fax.fax(document)

    def scan(self, document):
        self.scaner.scan(document)


if __name__ == '__main__':
    my_printer = MyPrinter()
    my_printer.print("some document")

    my_fax = MyFax()
    my_fax.fax("report")

    my_scanner = MyScanner()
    my_scanner.scan("photos")

    my_photocopier = PhotoCopier()
    my_photocopier.print("Esse")
    my_photocopier.scan("Photo")

    my_multi = MyMultifunctionMachine(my_printer, my_fax, my_scanner)
    my_multi.scan("Report1!!")
