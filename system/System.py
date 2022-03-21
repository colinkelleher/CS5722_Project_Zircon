import uuid
from abc import ABC, abstractmethod


class System(ABC):
    def __init__(self):
        self._system_id = uuid.uuid4()

    def __str__(self) -> str:
        return f"System has ID: {self._system_id}"

    def get_id(self):
        return self._system_id

    # @abstractmethod
    # def update(self, **kwargs):
    #     pass
