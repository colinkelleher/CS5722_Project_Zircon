from typing import List

from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Entity import Entity
from system.System import System


class DisplaySystem(System):
    def update(self, context, console, entities: List[Entity]):
        console.clear()

        for e in entities:
            dc = e.get(DisplayComponent)
            poscomp = e.get(PositionComponent)
            console.print(x=poscomp.x, y=poscomp.y, string=dc.character, bg=dc.color)

        context.present(console)  # Show the console.
