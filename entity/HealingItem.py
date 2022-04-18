from __future__ import annotations

import random
from abc import abstractmethod, ABC

import config
from command.setForegroundColorCommand import setForegroundColorCommand
from component.Component import Component
from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.WalkableComponent import WalkableComponent
from entity.Entity import Entity
from factory.RoomObject import RectangularRoom
from state.ItemInterface import Item
# from state.StateInterface import State
from command.Invoker import Invoker
from command.useHealingItemCommand import useHealingItemCommand


class HealingItem(Entity, Item):

    def __init__(self, x: int, y: int, state: State):
        super().__init__(
            DisplayComponent("H", config.bg_color_item, config.fg_color_item),
            PositionComponent(x, y),
            WalkableComponent(True)
        )
        self.transition_to(state)


def add_healing_item(new_room: RectangularRoom):
    x = random.randint(new_room.x1 + 2, new_room.x2 - 2)
    y = random.randint(new_room.y1 + 2, new_room.y2 - 2)
    item = HealingItem(x, y, NewState())
    pass


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


class SimpleState(State):

    def __init__(self):
        self.name = "Simple"

    def use_item(self, comp) -> None:
        print("Nothing happens.")

    def repair_item(self) -> None:
        print("Nothing happens.")


"""
"""


class NewState(State):

    def __init__(self):
        self.name = "New"

    def use_item(self, player_hp_comp) -> None:
        print("Item is used.\n")
        self.context.transition_to(UsedState())
        Invoker(useHealingItemCommand(player_hp_comp)).invoke()

    def repair_item(self) -> None:
        print("Item is already in NewState, nothing happens.\n")


"""
"""


class UsedState(State):

    def __init__(self):
        self.name = "Used"

    def use_item(self, player_hp_comp) -> None:
        print("Item is used.\n")
        self.context.transition_to(DamagedState())
        Invoker(useHealingItemCommand(player_hp_comp)).invoke()
        # Invoker(setForegroundColorCommand(player_dp_comp)).invoke()

    def repair_item(self) -> None:
        print("Item is repaired.\n")
        self.context.transition_to(NewState())


"""
"""


class DamagedState(State):

    def __init__(self):
        self.name = "Damaged"
        player_dp_comp = self.context.get(DisplayComponent)
        Invoker(setForegroundColorCommand(player_dp_comp)).invoke()

    def use_item(self, player_hp_comp) -> None:
        print("Item is in DamagedState, it can't be used, nothing happens.\n")

    def repair_item(self) -> None:
        print("Item is repaired.\n")
        self.context.transition_to(NewState())
