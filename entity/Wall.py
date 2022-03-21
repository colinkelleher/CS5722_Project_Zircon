from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Entity import Entity


class Wall(Entity):
    def __init__(self):
        super().__init__(DisplayComponent(" ", (150,150,150)), PositionComponent(20,20))