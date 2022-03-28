import uuid

from component.Component import Component
from memento.ConcreteMemento import ConcreteMemento
from memento.Memento import Memento


class Entity(object):
    entity_mapping = {}  # Maps entity IDs to entity objects

    def __init__(self, *components):
        self.id = str(uuid.uuid4())
        self.components = {}
        self.entity_mapping[self.id] = self

        for component in components:
            self.set_component(component)

    def set_component(self, component: Component):
        key = type(component)
        self.components[key] = component

    def get(self, class_name):
        return self.components[class_name]

    def has(self, class_name):
        return self.get(class_name) is not None

    @staticmethod
    def save() -> Memento:
        entities = Entity.entitymapping.values()
        return ConcreteMemento(entities)

    @staticmethod
    def restore(memento: ConcreteMemento) -> None:
        global_state = memento.get_state()
        for entity_id, components in global_state.items():
            entity = Entity.entitymapping[entity_id]
            for component_class, attributes in components.items():
                component = entity.get(component_class)
                component.__update_attr__(attributes)
