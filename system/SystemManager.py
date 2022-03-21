import uuid
from typing import List, Dict

from system import System


class SystemManager:
    def __init__(self):
        self.systemList: Dict[uuid.UUID, System] = {}

    def set_system(self, system: System):
        self.systemList[system.get_id(self)] = system


    def update(self, *args):
        for system in self.systemList.values():
            system.update(*args)
