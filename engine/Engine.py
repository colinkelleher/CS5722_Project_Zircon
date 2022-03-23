import os

import tcod

from definitions import ROOT_DIR
from entity.Floor import Floor
from entity.Wall import Wall
from system.FactoryMethod import GameMap
from system.SystemManager import SystemManager


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Engine(metaclass=SingletonMeta):
    # TODO must not take screen width, height and game map as parameters
    def __init__(self):
        self.entities = []

        # TODO put magical values like these in a config file
        WIDTH, HEIGHT = 80, 90  # Console width and height in tiles.
        # self.game_map = game_map

        """Script entry point."""
        # Load the font, a 32 by 8 tile font with libtcod's old character layout.
        path_to_tilesheet = os.path.join(ROOT_DIR, 'resources\\dejavu10x10_gs_tc.png')
        tileset = tcod.tileset.load_tilesheet(
            path_to_tilesheet, 32, 8, tcod.tileset.CHARMAP_TCOD,
        )
        # Create the main console.
        self.console = tcod.Console(WIDTH, HEIGHT, order="F")
        # Create a window based on this console and tileset.
        self.context = tcod.context.new(columns=self.console.width, rows=self.console.height, tileset=tileset)

        # Creation of System Manager and Systems
        self.system_manager = SystemManager()

        # Creation of Entities Wall and Floor
        # TODO must be moved away in a different system

        # grid = self.game_map.tiles
        # for i in range(len(grid) - 1):
        #     for j in range(len(grid) - 1):
        #         if grid[i][j] == 1:
        #             Wall(i, j)
        #         elif grid[i][j] == 0:
        #             Floor(i, j)
        #         else:
        #             pass

    # TODO should not pass self.entities, as entity list can be accessed from Entity.entitymapping static list
    def update(self):
        self.system_manager.update(self.context, self.console, self.entities)
