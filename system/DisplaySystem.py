from typing import List

from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Entity import Entity
from system.System import System


class DisplaySystem(System):
    def update(self, context, console, entities):
        console.clear()

        for e in entities:
            dc = e.get(DisplayComponent)
            poscomp = e.get(PositionComponent)
            console.print(x=poscomp.x, y=poscomp.y, string=dc.character, bg=dc.bg_color, fg=dc.fg_color)

        context.present(console)  # Show the console.
