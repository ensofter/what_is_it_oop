from __future__ import annotations
from abc import ABC, abstractmethod


class Editor:
    clipboard = None

    def __init__(self, text: str):
        self.text = text


class EditorCommand(ABC):

    def __init__(self, editor):
        self.editor = editor

    @abstractmethod
    def execute(self) -> None:
        pass


class CommandCopy(EditorCommand):
    __backup = None

    def __init__(self, editor: Editor):
        super().__init__(editor)

    def execute(self):
        self._backup()
        self.editor.clipboard = self.editor.text

    def rollback(self):
        self.editor.clipboard = self.__backup

    def _backup(self):
        self.__backup = self.editor.clipboard


class CommandPast(EditorCommand):
    __backup = None

    def __init__(self, editor: Editor):
        super().__init__(editor)

    def execute(self):
        self._backup()
        self.editor.text += self.editor.clipboard

    def rollback(self):
        self.editor.text = self.__backup

    def _backup(self):
        self.__backup = self.editor.text


if __name__ == '__main__':
    editor = Editor('some text for redactor')
    copy1 = CommandCopy(editor=editor)
    copy1.execute()
    print(editor.clipboard)
    print(editor.text)
    editor.text = 'haha'
    past1 = CommandPast(editor=editor)
    past1.execute()
    print(editor.text)
    copy2 = CommandCopy(editor=editor)
    editor.text += 'my name'
    copy2.execute()
    past2 = CommandPast(editor=editor)
    past2.execute()
    print(editor.text)

