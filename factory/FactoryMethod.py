from __future__ import annotations
from abc import ABC, abstractmethod


class MapGenerator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def create_map(self) -> str:

        game_map = self.factory_method()

        result = f"{game_map.create_walls()}"

        return result


class MapGeneratorSimple(MapGenerator):

    def factory_method(self) -> GameMap:
        return GameMapSimple()


def client_code(creator: MapGenerator) -> None:

    print(f"{creator.create_map()}")