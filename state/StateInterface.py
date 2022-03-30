from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):

    @property
    def context(self) -> Item:
        return self._context

    @context.setter
    def context(self, context: Item) -> None:
        self._context = context

    @abstractmethod
    def use_item(self) -> None:
        pass

    @abstractmethod
    def repair_item(self) -> None:
        pass


"""
"""


class Item:
    _state = None

    def transition_to(self, state: State):
        if self._state is None:
            print(f"Item creation, state set to {type(state).__name__}")
        else:
            print(f"Item: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def use_action(self):
        self._state.use_item()

    def fix_action(self):
        self._state.repair_item()

# if __name__ == "__main__":
#
#     test_item = Item(NewState())
#     test_item.use_action()
#     test_item.use_action()
#     test_item.fix_action()
#     test_item.fix_action()
