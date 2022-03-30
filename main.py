import tcod

from command.useHealingItemCommand import useHealingItemCommand
from component.PositionComponent import PositionComponent
from component.HpComponent import HpComponent
from engine.Engine import Engine
from entity.SimpleItem import SimpleItem
from state.States import SimpleState, DamagedState
from system.DisplaySystem import DisplaySystem
from command.exitCommand import exitCommand
from command.Invoker import Invoker
from command.rightCommand import rightCommand
from command.leftCommand import leftCommand
from command.upCommand import upCommand
from command.downCommand import downCommand


class Main:
    def __init__(self):
        self.engine = Engine()
        display_system = DisplaySystem()
        self.engine.system_manager.set_system(display_system)

    def core_game_loop(self):

        while True:
            self.engine.update()
            # This event loop will wait until at least one event is processed before exiting.
            # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
            for event in tcod.event.wait():
                self.engine.context.convert_event(event)  # Sets tile coordinates for mouse events.
                print(event)  # Print event names and attributes.

                player = self.engine.player
                player_pos_comp = player.get(PositionComponent)  # Get displayComponent for the single Entity
                player_hp_comp = player.get(HpComponent)
                if isinstance(event, tcod.event.KeyDown):  # later we should have many entities
                    key = event.sym
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
                        player.healing_item.use_action(player_hp_comp)
                if isinstance(event, tcod.event.Quit):
                    Invoker(exitCommand()).invoke()

                # The window will be closed after the above with-block exits.

                # TO DO:  put all the input code in a Command Pattern which
                #  should work for all the Entities (not only one like here )


if __name__ == "__main__":
    main = Main()
    main.core_game_loop()

