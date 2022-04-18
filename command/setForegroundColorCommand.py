import config
from command.Command import Command
from component.DisplayComponent import DisplayComponent


class setForegroundColorCommand(Command):
    def __init__(self, dp_comp: DisplayComponent):
        self.dp_comp = dp_comp

    def execute(self):
        self.dp_comp.set_fg_color(config.fg_color_item_damaged)
        print("Item color changed.")

    def undo(self) -> None:
        pass
