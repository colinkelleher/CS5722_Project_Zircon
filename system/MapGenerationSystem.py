from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple, List, TYPE_CHECKING
import random
import numpy


if TYPE_CHECKING:
    from entity import Entity


class GameMap:
    """
    The goal of the GameMap is to be able to identify the type of tile by using a grid of numbers
    0 is a simple floor
    1 is a wall
    Other types can be added, for example 2: lava, 3: swamp...
    These numbers can then be used by the entities to calculate collision when the player move for example
    """
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = numpy.ones((width, height), int)  # grid full of 1

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height


class GameMapSimple(GameMap):
    """   Simple map is made of 0 and 1 (floor and wall)   """
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def in_bounds(self, x: int, y: int) -> bool:
        return super().in_bounds(x, y)


class GameMapComplex(GameMap):
    """   """
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def in_bounds(self, x: int, y: int) -> bool:
        return super().in_bounds(x, y)


class DungeonGenerator(ABC):
    """"""
    @abstractmethod
    def generate_dungeon(self, max_rooms: int, room_min_size: int, room_max_size: int, map_width: int, map_height: int,
                         player: Entity) -> GameMap:
        pass


class DungeonGeneratorRectangle(DungeonGenerator):
    def generate_dungeon(self, max_rooms: int, room_min_size: int, room_max_size: int, map_width: int, map_height: int,
                         player: Entity) -> GameMap:

        dungeon = GameMapSimple(map_width, map_height)

        rooms: List[RectangularRoom] = []

        for r in range(max_rooms):
            # room size
            room_width = random.randint(room_min_size, room_max_size)
            room_height = random.randint(room_min_size, room_max_size)
            # room top left corner position
            x = random.randint(0, dungeon.width - room_width - 1)
            y = random.randint(0, dungeon.height - room_height - 1)
            # room creation
            new_room = RectangularRoom(x, y, room_width, room_height)
            # Run through the other rooms and see if they intersect with this one.
            if any(new_room.intersects(room2) for room2 in rooms):
                continue  # This room intersects, so go to the next attempt.
            # If there are no intersections then the room is valid.

            # dig this room inner area by replacing 1 by 0
            for i in range(x+room_width):
                for j in range(y+room_height):
                    dungeon.tiles[i, j] = 0

            # for the first room created, the player is placed in the center
            # the next rooms are linked by tunnels
            if len(rooms) == 0:
                player.x, player.y = new_room.center
            # TO-DO: add the code here to draw the tunnels between those rooms

            # put the room in the list
            rooms.append(new_room)

        return dungeon


class DungeonGeneratorOther(DungeonGenerator):
    def generate_dungeon(self, max_rooms: int, room_min_size: int, room_max_size: int, map_width: int, map_height: int,
                         player: Entity) -> GameMap:

        dungeon = GameMapComplex(map_width, map_height)

        rooms: List[OtherRoom] = []

        for r in range(max_rooms):
            # room external size
            room_width = random.randint(room_min_size, room_max_size)
            room_height = random.randint(room_min_size, room_max_size)

            x = random.randint(0, dungeon.width - room_width - 1)
            y = random.randint(0, dungeon.height - room_height - 1)

            new_room = OtherRoom(x, y, room_width, room_height)

            if any(new_room.intersects(room2) for room2 in rooms):
                continue

            # Here is the code difference
            # TO-DO: how to dig the inner part of the room in the GameMap
            # for i in range(x+room_width):
            #    for j in range(y+room_height):
            #        dungeon.tiles[i, j] = 0

            if len(rooms) == 0:
                player.x, player.y = new_room.center

            rooms.append(new_room)

        return dungeon


class Room(object):
    """
    Regular room
    x,y is the top left corner position
    The difference between the subclasses of Room is the walls positioning
    RectangleRom is a simple room with walls in the shape of a rectangle
    Other types of rooms can have more walls inside the room for example
    """
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        pass

    def center(self):
        pass

    def inner(self):
        pass

    def intersects(self, other_room: Room):
        pass


class RectangularRoom(Room):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, room: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
                self.x1 <= room.x2
                and self.x2 >= room.x1
                and self.y1 <= room.y2
                and self.y2 >= room.y1
        )


class OtherRoom(Room):

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)

    def center(self):
        super().center()

    def inner(self):
        super().inner()

    def intersects(self, room: OtherRoom):
        super().intersects(room)
