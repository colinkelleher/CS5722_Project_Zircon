from command.Command import Command
from command.Invoker import Invoker
from component.HpComponent import HpComponent


class useHealingItemCommand(Command):
    def __init__(self, hp_comp: HpComponent):
        self.hp_comp = hp_comp

    def execute(self):
        self.hp_comp.increase_hp(5)
        print("Player health increased.")

    def undo(self) -> None:
        from command.decreaseHpCommand import decreaseHpCommand
        Invoker(decreaseHpCommand(self.hp_comp)).invoke()
