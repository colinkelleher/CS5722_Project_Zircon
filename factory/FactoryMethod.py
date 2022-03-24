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


class GameMap(ABC):
    """
    The GameMap goal is creating Floor entities,
    following some pattern depending on what concrete GameMap creator is used
    """
    @abstractmethod
    def create_walls(self) -> str:
        pass


class GameMapSimple(GameMap, ABC):
    """
    The GameMapSimple creates only Floor tiles to draw rectangle shapes
    """
    def create_walls(self) -> str:
        # Add here the code to create the walls needed for rectangle rooms
        return "Simple Map is used."


def client_code(creator: MapGenerator) -> None:

    print(f"{creator.create_map()}")