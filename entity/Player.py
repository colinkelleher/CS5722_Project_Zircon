from component.DisplayComponent import DisplayComponent
from entity.Entity import Entity


class Player(Entity):
     def __init__(self):
        super().__init__(DisplayComponent("@"))
