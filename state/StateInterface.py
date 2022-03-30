from __future__ import annotations
from abc import ABC, abstractmethod

from component.Component import Component


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


class Item:
    _state = None

    def transition_to(self, state: State):
        if self._state is None:
            print(f"Item creation, state set to {type(state).__name__}")
        else:
            print(f"Item: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def use_action(self, player_hp_comp: Component):
        self._state.use_item(player_hp_comp)

    def fix_action(self):
        self._state.repair_item()

# if __name__ == "__main__":
#
#     test_item = Item(NewState())
#     test_item.use_action()
#     test_item.use_action()
#     test_item.fix_action()
#     test_item.fix_action()
