import config
from command.Invoker import Invoker
from command.setForegroundColorCommand import setForegroundColorCommand
from command.useHealingItemCommand import useHealingItemCommand
from entity.HealingItem import State


"""


class SimpleState(State):

    def __init__(self):
        self.name = "Simple"

    def use_item(self, comp) -> None:
        print("Nothing happens.")

    def repair_item(self) -> None:
        print("Nothing happens.")


class NewState(State):

    def __init__(self):
        self.name = "New"

    def use_item(self, player_hp_comp) -> None:
        print("Item is used.\n")
        self.context.transition_to(UsedState())
        Invoker(useHealingItemCommand(player_hp_comp)).invoke()

    def repair_item(self) -> None:
        print("Item is already in NewState, nothing happens.\n")


class UsedState(State):

    def __init__(self):
        self.name = "Used"

    def use_item(self, player_hp_comp) -> None:
        print("Item is used.\n")
        self.context.transition_to(DamagedState())
        Invoker(useHealingItemCommand(player_hp_comp)).invoke()
        # Invoker(setForegroundColorCommand(player_dp_comp)).invoke()

    def repair_item(self) -> None:
        print("Item is repaired.\n")
        self.context.transition_to(NewState())


class DamagedState(State):

    def __init__(self):
        self.name = "Damaged"
        # set_fg_color(config.fg_color_item_damaged)
        # player_dp_comp = self.context.get(DisplayComponent)
        # Invoker(setForegroundColorCommand(player_dp_comp)).invoke()

    def use_item(self, player_hp_comp) -> None:
        print("Item is in DamagedState, it can't be used, nothing happens.\n")

    def repair_item(self) -> None:
        print("Item is repaired.\n")
        self.context.transition_to(NewState())
        
        
 """