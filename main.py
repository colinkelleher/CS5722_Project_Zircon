import tcod

from component.DisplayComponent import DisplayComponent
from engine.Engine import Engine
from entity.Player import Player
from system.DisplaySystem import DisplaySystem


class Main:
    def __init__(self):
        self.engine = Engine()
        self.player = Player()
        self.engine.add_entity(self.player)
        display_system = DisplaySystem()
        self.engine.add_system(display_system)

    def core_game_loop(self):

        while True:

            self.engine.update()

            # This event loop will wait until at least one event is processed before exiting.
            # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
            for event in tcod.event.wait():
                self.engine.context.convert_event(event)  # Sets tile coordinates for mouse events.
                print(event)  # Print event names and attributes.

                dc = self.player.get(DisplayComponent)  # Get displayComponent for the single Entity
                if isinstance(event, tcod.event.KeyDown):  # later we should have many entities
                    key = event.sym
                    if key == tcod.event.K_UP:
                        dc.y -= 1
                    elif key == tcod.event.K_DOWN:
                        dc.y += 1
                    elif key == tcod.event.K_LEFT:
                        dc.x -= 1
                    elif key == tcod.event.K_RIGHT:
                        dc.x += 1
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()

                # The window will be closed after the above with-block exits.

                # TO DO:  put all the input code in a Command Pattern which
                #  should work for all the Entities (not only one like here )


if __name__ == "__main__":
    main = Main()
    main.core_game_loop()
