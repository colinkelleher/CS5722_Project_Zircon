from builder.EntityBuilder import EntityBuilder
from component.DisplayComponent import DisplayComponent
from component.HpComponent import HpComponent
from component.PositionComponent import PositionComponent
from entity.Enemy import Enemy


class GenericEasyEnemyBuilder(EntityBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._enemy = Enemy()

    @property
    def product(self) -> Enemy:
        # Builders are expected to start fresh everytime, so we use reset once we retrieve the enemy produced in order
        # to clean everything up
        product = self._enemy
        self.reset()
        return product

    def add_position_component(self) -> None:
        position_component = PositionComponent()
        self._enemy.set_component(position_component)

    def add_display_component(self) -> None:
        display_component = DisplayComponent(character="o", color=(186, 14, 14))
        self._enemy.set_component(display_component)

    def add_hp_component(self) -> None:
        hp_component = HpComponent(hp_value=50)
        self._enemy.set_component(hp_component)
