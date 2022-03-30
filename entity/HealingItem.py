import random

import config
from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.WalkableComponent import WalkableComponent
from entity.Entity import Entity
from factory.RoomObject import RectangularRoom
from state.StateInterface import State, Item
from state.States import NewState


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
