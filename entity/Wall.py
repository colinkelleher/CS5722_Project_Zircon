import config
from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.WalkableComponent import WalkableComponent
from entity.Entity import Entity


class Wall(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(
            DisplayComponent(" ", config.bg_color_wall, config.fg_color_wall),
            PositionComponent(x, y),
            WalkableComponent(False)
        )
