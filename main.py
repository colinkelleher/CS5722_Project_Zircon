import tcod

from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from engine.Engine import Engine
from entity.Player import Player
from entity.Wall import Wall
from system.DisplaySystem import DisplaySystem
from system.MapGenerationSystem import DungeonGenerator


class Main:
    def __init__(self):

        # these next lines should be moved out of the Main class
        screen_width = 80
        screen_height = 90
        self.player = Player(int(screen_width / 2), int(screen_height / 2))
        # dg = DungeonGenerator()
        # game_map = DungeonGenerator.generate_dungeon(dg, max_rooms=20, room_min_size=6, room_max_size=20,
        # map_width=80, map_height=80, player=self.player)
        self.wall_determined = Wall(25, 25)

        self.engine = Engine(screen_width, screen_height)
        self.engine.add_entity(self.player)
        self.engine.add_entity(self.wall_determined)
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
