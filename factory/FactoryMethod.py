from __future__ import annotations
from abc import ABC, abstractmethod

from factory.GameMapCreator import GameMap, GameMapSimple


class MapGenerator(ABC):  # Factory interface

    @abstractmethod
    def factory_method(self):
        pass

    def create_map(self) -> str:
        game_map = self.factory_method()

        result = f"{game_map.create_walls()}"

        return result


class MapGeneratorSimple(MapGenerator):  # Concrete Factory

    def factory_method(self) -> GameMap:
        return GameMapSimple()
