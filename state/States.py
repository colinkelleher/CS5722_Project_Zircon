from command.Invoker import Invoker
from command.useHealingItemCommand import useHealingItemCommand
from state.StateInterface import State


"""
"""


class SimpleState(State):
    def use_item(self) -> None:
        print("Nothing happens.")

    def repair_item(self) -> None:
        print("Nothing happens.")


"""
"""


class NewState(State):
    def use_item(self, player_hp_comp) -> None:
        print("Item is used.")
        self.context.transition_to(UsedState())
        Invoker(useHealingItemCommand(player_hp_comp)).invoke()

    def repair_item(self) -> None:
        print("Item is already in NewState, nothing happens.")


"""
"""


class UsedState(State):
    def use_item(self, player_hp_comp) -> None:
        print("Item is used.")
        self.context.transition_to(DamagedState())
        Invoker(useHealingItemCommand(player_hp_comp)).invoke()

    def repair_item(self) -> None:
        print("Item is repaired.")
        self.context.transition_to(NewState())


"""
"""


class DamagedState(State):
    def use_item(self, player_hp_comp) -> None:
        print("Item is in DamagedState, it can't be used, nothing happens.")

    def repair_item(self) -> None:
        print("Item is repaired.")
        self.context.transition_to(NewState())
