from __future__ import annotations
from abc import ABC, abstractmethod

from component.Component import Component
from state.ItemInterface import Item


class State(ABC):

    @property
    def context(self) -> Item:
        return self._context

    @context.setter
    def context(self, context: Item) -> None:
        self._context = context

    @abstractmethod
    def use_item(self, comp: Component) -> None:
        pass

    @abstractmethod
    def repair_item(self) -> None:
        pass


"""
"""
