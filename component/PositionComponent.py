from component.Component import Component


class PositionComponent(Component):
    def __init__(self, x: int = None, y: int = None):
        self.x = x
        self.y = y

    def set_pos(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_pos_x(self, x: int):
        self.x = x

    def set_pos_y(self, y: int):
        self.y = y

    def get_pos_x(self) -> int:
        return self.x

    def get_pos_y(self) -> int:
        return self.y
