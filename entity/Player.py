import config
from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.HpComponent import HpComponent
from entity.Entity import Entity
from entity.HealingItem import HealingItem
from state.States import NewState


class Player(Entity):
    def __init__(self, x: int = None, y: int = None):
        super().__init__(
            DisplayComponent("@", config.bg_color_player, config.fg_color_player),
            PositionComponent(x, y),
            HpComponent()
        )
        self.healing_item = HealingItem(20, 65, NewState())
