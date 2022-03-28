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
        # self.entities = Entity.entity_mapping
        self.entities = []
        self.screen_width = config.screen_width
        self.screen_height = config.screen_height
        self.tileset = config.tileset

        """Script entry point."""
        # Create the main console.
        self.console = tcod.Console(self.screen_width, self.screen_height, order="F")
        # Create a window based on this console and tileset.
        self.context = tcod.context.new(columns=self.console.width, rows=self.console.height, tileset=self.tileset)

        # Creation of System Manager and Systems
        self.system_manager = SystemManager()

        # Creation of the map
        print("\n")
        client_code(MapGeneratorSimple())
        print("\n")

    # TODO should not pass self.entities, as entity list can be accessed from Entity.entitymapping static list
    def update(self):
        self.system_manager.update(self.context, self.console, self.entities)
