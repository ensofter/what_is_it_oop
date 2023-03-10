from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def checkbox(self):
        pass


class ElementFabric(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


