from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Entity import Entity


class Player(Entity):
     def __init__(self):
        super().__init__(DisplayComponent("@", (ord(" "), (255, 255, 255), (0, 0, 0))), PositionComponent(25, 25))
