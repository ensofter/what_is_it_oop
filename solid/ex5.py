from abc import ABC, abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name: str):
        self.name = name


class RelationBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name: str):
        pass


class RelationStorage(RelationBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name: str):
        for i in self.relations:
            if i[0].name == name and i[1] == Relationship.PARENT:
                yield i[2].name


class Research:
    # def __init__(self, relations: RelationStorage):
    #     self.relations = relations.relations
    #     for i in self.relations:
    #         if i[0].name == "John" and i[1] == Relationship.PARENT:
    #             print(f"John is parent of {i[2].name}")

    def __init__(self, browser: RelationBrowser):
        for p in browser.find_all_children_of('John'):
            print(f"John is parent of {p}")


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Fill')
    child2 = Person('Sofi')

    relationships = RelationStorage()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    research = Research(relationships)