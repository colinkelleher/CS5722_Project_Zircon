from component.Component import Component
from typing import Tuple


class DisplayComponent(Component):
    def __init__(self, character: str, color: Tuple[int, int, int]):
        self.character = character
        self.color = color

    """
    Color represents the tile background color
    We can differentiate later the tiles that are in or out of the field of view (FOV) 
    and change the background color
    """
    def set_color(self, color: Tuple[int, int, int]):
        self.color = color
