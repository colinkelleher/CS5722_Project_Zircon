from command.Command import Command
from command.Invoker import Invoker


class decreaseHpCommand(Command):
    def __init__(self, hp_comp):
        self.hp_comp = hp_comp

    def execute(self):
        self.hp_comp.increase_hp(-5)
        print("Player health decreased.")

    def undo(self) -> None:
        from command.useHealingItemCommand import useHealingItemCommand
        Invoker(useHealingItemCommand(self.hp_comp)).invoke()
