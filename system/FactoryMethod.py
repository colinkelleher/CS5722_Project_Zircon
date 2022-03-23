from __future__ import annotations
from abc import ABC, abstractmethod


class MapGenerator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:

        product = self.factory_method()

        result = f"{product.operation()}"

        return result


class MapGeneratorSimple(MapGenerator):

    def factory_method(self) -> GameMap:
        return GameMapSimple()


class MapGeneratorComplex(MapGenerator):
    def factory_method(self) -> GameMap:
        return GameMapComplex()


class GameMap(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class GameMapSimple(GameMap):
    def operation(self) -> str:
        return "Simple Map is used."


class GameMapComplex(GameMap):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: MapGenerator) -> None:

    print(f"{creator.some_operation()}", end="")