from component.Component import Component
from typing import Tuple


class DisplayComponent(Component):
    def __init__(self, character: str, bg_color: Tuple[int, int, int], fg_color: Tuple[int, int, int]):
        self.character = character
        self.bg_color = bg_color
        self.fg_color = fg_color

    """
    Color represents the tile background color
    We can differentiate later the tiles that are in or out of the field of view (FOV) 
    and change the background color
    """
    def set_bg_color(self, bg_color: Tuple[int, int, int]):
        self.bg_color = bg_color

    def set_fg_color(self, fg_color: Tuple[int, int, int]):
        self.fg_color = fg_color
