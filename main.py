import tcod

from component.PositionComponent import PositionComponent
from engine.Engine import Engine
from entity.Player import Player
from entity.Wall import Wall
from system.DisplaySystem import DisplaySystem
from factory.FactoryMethod import client_code, MapGeneratorSimple


class Main:
    def __init__(self):
        screen_width = 80
        screen_height = 90
        self.player = Player(int(screen_width / 2), int(screen_height / 2))
        print("\n")
        client_code(MapGeneratorSimple())
        print("\n")

        # map_width, map_height, room_max_size, room_min_size, max_rooms = 80, 80, 20, 6, 30
        # game_map = generate_dungeon(
        #     max_rooms=max_rooms,
        #     room_min_size=room_min_size,
        #     room_max_size=room_max_size,
        #     map_width=map_width,
        #     map_height=map_height,
        #     player=self.player
        # )

        self.wall_determined = Wall(25, 25)
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
