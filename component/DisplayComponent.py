from component.Component import Component


class DisplayComponent(Component):
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.character = character
