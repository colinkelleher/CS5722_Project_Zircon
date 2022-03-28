from typing import List

from entity.Entity import Entity
from memento.Memento import Memento


class Caretaker:

    def __init__(self) -> None:
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        print("\nCaretaker: Saving Game Entities' state...")
        self._mementos.append(Entity.save())

    def undo(self) -> None:
        if not self._mementos:
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            Entity.restore(memento)
        except Exception:
            self.undo()


    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())

    def get_memento_name(self, index: int) -> str:
        memento = self._mementos[index]
        memento_name = memento.get_name()
        return str(memento_name)
