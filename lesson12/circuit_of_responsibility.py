from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class LoadHandler(ABC):

    @abstractmethod
    def set_next(self, handler: LoadHandler) -> LoadHandler:
        pass

    @abstractmethod
    def handle(self, request: dict) -> bool:
        pass


class AbstractLoadHandler(LoadHandler):
    _next_handler: LoadHandler = None

    def set_next(self, handler: LoadHandler) -> LoadHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> bool:
        if self._next_handler:
            return self._next_handler.handle(request)
        return True

