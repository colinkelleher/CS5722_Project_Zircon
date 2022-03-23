from builder.EntityBuilder import EntityBuilder


class Director:
    def __init__(self) -> None:
        self._entity_builder = None

    @property
    def entity_builder(self) -> EntityBuilder:
        return self._entity_builder

    @entity_builder.setter
    def entity_builder(self, entity_builder: EntityBuilder):
        self._entity_builder = entity_builder

    def build_entity_with_position_only(self) -> None:
        self.entity_builder.add_position_component()

    def build_complete_entity(self) -> None:
        self.entity_builder.add_position_component()
        self.entity_builder.add_hp_component()
        self.entity_builder.add_display_component()
