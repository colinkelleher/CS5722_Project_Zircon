from component.Component import Component


class DisplayComponent(Component):
    def __init__(self, character, dark: tuple[int, int, int]):
        self.character = character
        self.dark = dark

    """
    Dark represents the tile color, for now
    We will add later the Light that is a new color for the tile, depending if
    it is in the field of view (FOV)
    """
    def set_dark(self, dark: tuple[int, int, int]):
        self.dark = dark
