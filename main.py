import tcod

import config
from component.PositionComponent import PositionComponent
from engine.Engine import Engine
from entity.Player import Player
from system.DisplaySystem import DisplaySystem


class Main:
    def __init__(self):
        screen_width = config.screen_width
        screen_height = config.screen_height
        self.player = Player(int(screen_width / 2), int(screen_height / 2))

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

                poscomp = self.player.get(PositionComponent)  # Get displayComponent for the single Entity
                if isinstance(event, tcod.event.KeyDown):  # later we should have many entities
                    key = event.sym
                    if key == tcod.event.K_UP:
                        poscomp.y -= 1
                    elif key == tcod.event.K_DOWN:
                        poscomp.y += 1
                    elif key == tcod.event.K_LEFT:
                        poscomp.x -= 1
                    elif key == tcod.event.K_RIGHT:
                        poscomp.x += 1
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()

                # The window will be closed after the above with-block exits.

                # TO DO:  put all the input code in a Command Pattern which
                #  should work for all the Entities (not only one like here )


if __name__ == "__main__":
    main = Main()
    main.core_game_loop()
