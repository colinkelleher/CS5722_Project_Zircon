from typing import List

import tcod

from component.HpComponent import HpComponent
from component.PositionComponent import PositionComponent
from engine.Engine import SingletonMeta
from entity.Player import Player
from events import Events
from events.Events import Event
from command.exitCommand import exitCommand
from command.Invoker import Invoker
from command.rightCommand import rightCommand
from command.leftCommand import leftCommand
from command.upCommand import upCommand
from command.downCommand import downCommand
from command.useHealingItemCommand import useHealingItemCommand


class EventManager:
    pass


class InputManager(EventManager, metaclass=SingletonMeta):
    def __init__(self, player: Player):
        self.player = player

    def handle_input(self, event: tcod.event.KeyDown):
        key = event.sym
        player_pos_comp = self.player.get(PositionComponent)  # Get displayComponent for the single Entity
        player_hp_comp = self.player.get(HpComponent)

        if key == tcod.event.K_UP:
            Invoker(upCommand(player_pos_comp)).invoke()
        elif key == tcod.event.K_DOWN:
            Invoker(downCommand(player_pos_comp)).invoke()
        elif key == tcod.event.K_LEFT:
            Invoker(leftCommand(player_pos_comp)).invoke()
        elif key == tcod.event.K_RIGHT:
            Invoker(rightCommand(player_pos_comp)).invoke()
        elif key == tcod.event.K_ESCAPE:
            Invoker(exitCommand()).invoke()
        elif key == tcod.event.K_h:
            Invoker(useHealingItemCommand(self.player.healing_item.use_action(player_hp_comp)))
            # self.player.healing_item.use_action(player_hp_comp)
        

