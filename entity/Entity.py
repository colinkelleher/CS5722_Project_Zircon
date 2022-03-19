import uuid
from typing import List

from component.Component import Component


class Entity(object):
    entitymapping = {}        # Maps entity IDs to entity objects

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.components: List[Component] = []
        self.entityindex[self.id] = self
