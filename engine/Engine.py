import os

import tcod

import config
from definitions import ROOT_DIR
from entity.Entity import Entity
from entity.Player import Player
from factory.FactoryMethod import client_code, MapGeneratorSimple
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

    def __init__(self):
        self.entities = []

        # Console width and height in tiles.
        self.screen_width = config.screen_width
        self.screen_height = config.screen_height

        """Script entry point."""
        # Load the font, a 32 by 8 tile font with libtcod's old character layout.
        tileset = config.tileset
        # Create the main console.
        self.console = tcod.Console(self.screen_width, self.screen_height, order="F")
        # Create a window based on this console and tileset.
        self.context = tcod.context.new(columns=self.console.width, rows=self.console.height, tileset=tileset)

        # Creation of System Manager and Systems
        self.system_manager = SystemManager()

        # Creation of Entities Wall and Floor
        print("\n")
        client_code(MapGeneratorSimple())
        print("\n")

        self.player = Player(int(self.screen_width / 2), int(self.screen_height / 2))

    # TODO should not pass self.entities, as entity list can be accessed from Entity.entitymapping static list
    def update(self):
        self.system_manager.update(self.context, self.console, Entity.entitymapping.values())
