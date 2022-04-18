import random

import config
from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.WalkableComponent import WalkableComponent
from entity.Entity import Entity
from entity.HealingItem import State, SimpleState
from factory.RoomObject import RectangularRoom
from state.ItemInterface import Item


class SimpleItem(Entity, Item):

    def __init__(self, x: int, y: int, state: State):
        super().__init__(
            DisplayComponent("i", config.bg_color_item, config.fg_color_item),
            PositionComponent(x, y),
            WalkableComponent(True)
        )
        self.transition_to(state)


def add_simple_item(new_room: RectangularRoom):
    x = random.randint(new_room.x1 + 2, new_room.x2 - 2)
    y = random.randint(new_room.y1 + 2, new_room.y2 - 2)
    item = SimpleItem(x, y, SimpleState())
    pass
