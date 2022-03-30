import config
from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.HpComponent import HpComponent
from entity.Entity import Entity


class Player(Entity):
    def __init__(self, x: int = None, y: int = None):
        super().__init__(
            DisplayComponent("@", config.bg_color_player, config.fg_color_player),
            PositionComponent(x, y),
            HpComponent()
        )
