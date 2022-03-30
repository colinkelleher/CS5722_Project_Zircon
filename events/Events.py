from dataclasses import dataclass

import tcod.event


class Event:
    pass


@dataclass
class MovementInput(Event):
    input: tcod.event.KeyDown
