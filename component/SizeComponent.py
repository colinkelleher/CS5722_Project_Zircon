from component.Component import Component


class SizeComponent(Component):
    def __init__(self, width: int = None, height: int = None):
        self.width = width
        self.height = height

    def set_pos(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_pos_x(self, width: int):
        self.width = width

    def set_pos_y(self, height: int):
        self.height = height
