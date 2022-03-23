from entity.Entity import Entity


class Enemy(Entity):
    def __init__(self, *components):
        super().__init__(*components)
