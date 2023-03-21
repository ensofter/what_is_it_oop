from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str):
        self._item_name: str = name
        self._owner_name: str = None

    def set_owner(self, o: str):
        self._owner_name = o

    @abstractmethod
    def add(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def remove(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def display(self):
        pass


class ClickableItem(Item):
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, sub_item: Item):
        raise Exception('кликабельному элементу нельзя добавить подэлементы')

    def remove(self, sub_item: Item):
        raise Exception('у кликабельного элемента не может быть подэлементов')

    def display(self):
        print(self._owner_name + self._item_name)


class DropDownItem(Item):
    def __init__(self, name: str):
        super().__init__(name)
        self.__children = []

    def add(self, sub_item: Item):
        sub_item.set_owner(self._item_name)
        self.__children.append(sub_item)

    def remove(self, sub_item: Item):
        self.__children.remove(sub_item)

    def display(self):
        for item in self.__children:
            if self._owner_name is not None:
                print(self._owner_name, end='')
            item.display()


if __name__ == '__main__':
    file: Item = DropDownItem('файл->')

    create: Item = DropDownItem('создать->')
    open: Item = DropDownItem('открыть->')
    exit: Item = ClickableItem('выход')

    file.add(create)
    file.add(open)
    file.add(exit)

    project: Item = ClickableItem('проект...')
    repository: Item = ClickableItem('репозиторий...')

    create.add(project)
    create.add(repository)

    solution: Item = ClickableItem('решение...')
    folder: Item = ClickableItem('папка...')

    open.add(solution)
    open.add(folder)

    file.display()
    print()
    file.remove(create)

    file.display()