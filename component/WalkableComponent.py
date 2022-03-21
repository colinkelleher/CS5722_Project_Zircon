from component.Component import Component


class WalkableComponent(Component):
    def __init__(self, walkable: bool = True):
        self.walkable = walkable

    def set_walkable(self, walkable: bool):
        self.walkable = walkable

    def get_walkable(self):
        return self.walkable
