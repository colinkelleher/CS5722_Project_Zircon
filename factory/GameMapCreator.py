from abc import ABC, abstractmethod

from entity.Floor import Floor
from entity.Wall import Wall


class GameMap(ABC):  # Creator interface
    """
    The GameMap goal is creating Floor entities,
    following some pattern depending on what concrete GameMap creator is used
    """

    @abstractmethod
    def create_walls(self) -> str:
        pass


class GameMapSimple(GameMap, ABC):  # Concrete creator
    """
    The GameMapSimple creates only Floor tiles to draw rectangle shapes
    """

    def create_walls(self) -> str:
        # Add here the code to create the walls needed for rectangle rooms

        wall_determined = Wall(25, 25)
        floor_determined = Floor(25, 26)

        return "Simple Map is used."
