from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class EntityBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_position_component(self) -> None:
        pass

    @abstractmethod
    def add_display_component(self) -> None:
        pass

    @abstractmethod
    def add_hp_component(self) -> None:
        pass
