from component.Component import Component


class PositionComponent(Component):
    def __init__(self):
        self.x = None
        self.y = None

    def set_pos(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_pos_x(self, x: int):
        self.x = x

    def set_pos_y(self, y: int):
        self.y = y