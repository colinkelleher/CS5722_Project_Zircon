from abc import ABC, abstractmethod


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
