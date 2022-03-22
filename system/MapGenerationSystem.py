from __future__ import annotations

from array import array

from typing import Tuple, List, TYPE_CHECKING
import random

from comtypes.safearray import numpy

if TYPE_CHECKING:
    from entity import Entity


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = numpy.ones((width, height), int)  # grid full of 1

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, other: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
                self.x1 <= other.x2
                and self.x2 >= other.x1
                and self.y1 <= other.y2
                and self.y2 >= other.y1
        )


def generate_dungeon(
        max_rooms: int,
        room_min_size: int,
        room_max_size: int,
        map_width: int,
        map_height: int,
        player: Entity,
) -> GameMap:
    dungeon = GameMap(map_width, map_height)

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
        if any(new_room.intersects(other_room) for other_room in rooms):
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

        # put the room in the list
        rooms.append(new_room)

    return dungeon
