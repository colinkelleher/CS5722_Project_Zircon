from typing import List

from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Entity import Entity
from system.System import System


class DisplaySystem(System):
    def update(self, context, console, entities: List[Entity]):
        console.clear()
        console.print(x=0, y=0, string="Hello World!")

        for e in entities:
            dc = e.get(DisplayComponent)
            poscomp = e.get(PositionComponent)
            console.print(x=poscomp.x, y=poscomp.y, string=dc.character)

        context.present(console)  # Show the console.
