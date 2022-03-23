from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Entity import Entity


class Player(Entity):
    def __init__(self, x: int = None, y: int = None):
        super().__init__(DisplayComponent("@", (0, 0, 0)), PositionComponent(x, y))
