from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from component.WalkableComponent import WalkableComponent
from entity.Entity import Entity


class Wall(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(DisplayComponent(" ", (100, 100, 100)), PositionComponent(x, y), WalkableComponent(False))
