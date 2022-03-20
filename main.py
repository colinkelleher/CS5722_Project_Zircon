import tcod


def main():
    WIDTH, HEIGHT = 80, 60  # Console width and height in tiles.
    player_x, player_y = (40, 25)
    """Script entry point."""
    # Load the font, a 32 by 8 tile font with libtcod's old character layout.
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
    )
    # Create the main console.
    console = tcod.Console(WIDTH, HEIGHT, order="F")
    # Create a window based on this console and tileset.
    with tcod.context.new(  # New window for a console of size columns×rows.
            columns=console.width, rows=console.height, tileset=tileset,
    ) as context:
        while True:  # Main loop, runs until SystemExit is raised.
            console.clear()
            console.print(x=0, y=0, string="Hello World!")
            console.print(x=player_x, y=player_y, string="@")
            context.present(console)  # Show the console.

            # This event loop will wait until at least one event is processed before exiting.
            # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                print(event)  # Print event names and attributes.
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                if isinstance(event, tcod.event.KeyDown):
                    key = event.sym
                    if key == tcod.event.K_UP:
                        player_y -= 1
                    elif key == tcod.event.K_DOWN:
                        player_y += 1
                    elif key == tcod.event.K_LEFT:
                        player_x -= 1
                    elif key == tcod.event.K_RIGHT:
                        player_x += 1

                        # The window will be closed after the above with-block exits.


if __name__ == "__main__":
    main()
