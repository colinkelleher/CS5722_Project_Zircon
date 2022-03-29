from __future__ import annotations

import copy
from abc import ABC, abstractmethod

import random
from typing import List, Tuple

import config
from component.PositionComponent import PositionComponent
from entity.Entity import Entity
from entity.Floor import Floor
from entity.Item import Item, add_item
from entity.Wall import Wall
from factory.RoomObject import RectangularRoom
from factory.TunnelObject import tunnel_between


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

        max_rooms = config.max_rooms
        room_min_size = config.room_min_size
        room_max_size = config.room_max_size
        map_width = config.map_width
        map_height = config.map_height

        rooms: List[RectangularRoom] = []

        for r in range(max_rooms):
            room_width = random.randint(room_min_size, room_max_size)
            room_height = random.randint(room_min_size, room_max_size)

            x = random.randint(0, map_width - room_width - 1)
            y = random.randint(0, map_height - room_height - 1)

            new_room = RectangularRoom(x, y, room_width, room_height)

            if any(new_room.intersects(other_room) for other_room in rooms):
                continue

            for i in range(x, x + room_width):
                for j in range(y, y + room_height):
                    room_wall = Wall(i, j)

            for i in range(x + 1, x + room_width - 1):
                for j in range(y + 1, y + room_height - 1):
                    room_floor = Floor(i, j)

            if len(rooms) == 0:
                pass
            else:
                pass
                # for x, y in tunnel_between(rooms[-1].center, new_room.center):
                #     tunnel_floor = Floor(x, y)

            # Add randomly 0, 1 or 2 Item in the room
            for i in range(random.randint(0, 2)):
                add_item(new_room)

            # Finally, append the new room to the list.
            rooms.append(new_room)

        # for i in range(map_width):
        #     for j in range(map_height):
        #         verify: int = len(rooms)
        #         for r in range(len(rooms)):
        #             # if (i < rooms[r].x1 or i > rooms[r].x2) and (j < rooms[r].y1 or j > rooms[r].y2):
        #             if (rooms[r].x1 < i < rooms[r].x2-1) and (rooms[r].y1 < j < rooms[r].y2-1):
        #                 verify -= 1
        #         if verify == len(rooms):
        #             map_wall = Wall(i, j)

        # floor_entities_dictionary = copy.deepcopy(Entity.entitymapping)
        # floor_entities = floor_entities_dictionary.values()
        # for i in range(map_width):
        #     for j in range(map_height):
        #         for e in floor_entities:
        #             # if type(e) == Wall:
        #             pc = e.get(PositionComponent)
        #             if (i != pc.x) and (j != pc.y):
        #                 map_wall = Wall(i, j)

        return "Simple Map is used."
