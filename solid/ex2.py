from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.size = size
        self.color = color
        self.name = name


class ProductFilter:

    @staticmethod
    def filter_by_color(products: [Product], color: Color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products: [Product], size: Size):
        for p in products:
            if p.size == size: yield p

    @staticmethod
    def filter_by_color_and_size(products: [Product], color:Color, size:Size):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# Specification

class Specification(ABC):

    @abstractmethod
    def is_satisfied(self, item: Product):
        pass


class Filter(ABC):

    @abstractmethod
    def filter(self, items: [Product], spec: Specification):
        pass


class ColorSpecification(Specification):

    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product):
        return item.size == self.size


class AndSpecification(Specification):

    def __init__(self, *args):
        self.specs = args

    def is_satisfied(self, item: Product):
        return all(map(lambda spec: spec.is_satisfied(item), self.specs))


class BetterFilter(Filter):

    def filter(self, items: [Product], spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product("apple", Color.GREEN, Size.SMALL)
    tree = Product("tree", Color.GREEN, Size.LARGE)
    house = Product("house", Color.BLUE, Size.LARGE)
    strawberry = Product("strawberry", Color.RED, Size.MEDIUM)

    products = [apple, tree, house, strawberry]

    print("ProductFilter realization")
    print("All large products")
    pf = ProductFilter()
    filtered = pf.filter_by_size(products, Size.LARGE)
    for i in filtered:
        print(f" - {i.name} is LARGE")

    print("\n")

    print("BetterFilter realization")
    print("All green products")
    bf = BetterFilter()
    spec = ColorSpecification(Color.GREEN)
    filtered = bf.filter(products, spec)
    for i in filtered:
        print(f" - {i.name} is GREEN")

    print("\n")

    print("Large and Blue items")
    medium = SizeSpecification(Size.MEDIUM)
    red = ColorSpecification(Color.RED)
    and_spec = AndSpecification(medium, red)
    filtered = bf.filter(products, and_spec)
    for i in filtered:
        print(f" - {i.name} medium AND red")
