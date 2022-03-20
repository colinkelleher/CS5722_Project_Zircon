import uuid
from typing import List

from component.Component import Component


class Entity(object):
    entitymapping = {}        # Maps entity IDs to entity objects

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.components = {}
        self.entitymapping[self.id] = self

    def set(self, component: Component):
        key = type(component)
        self.components[key] = component

    def get(self, class_name):
        return self.components[class_name]

    def has(self, class_name):
        return self.get(class_name) is not None





