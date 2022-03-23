from __future__ import annotations
from abc import ABC, abstractmethod

# Declares a method for executing a command

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass