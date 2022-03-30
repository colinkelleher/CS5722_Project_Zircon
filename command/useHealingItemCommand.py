from command.Command import Command


class useHealingItemCommand(Command):
    def __init__(self, hp_comp):
        self.hp_comp = hp_comp

    def execute(self):
        self.hp_comp.increase_hp(5)
        print("Player health increased by 5 points.")
