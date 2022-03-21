from typing import List

from component.DisplayComponent import DisplayComponent
from entity.Entity import Entity
from system.System import System


class DisplaySystem(System):
    def update(self, context, console, entities: List[Entity]):
        console.clear()
        console.print(x=0, y=0, string="Hello World!")

        for e in entities:
            dc = e.get(DisplayComponent)
            console.print(x=dc.x, y=dc.y, string=dc.character)

        context.present(console)  # Show the console.
