from command.Command import Command
from command.Invoker import Invoker


class upCommand(Command):
    def __init__(self, poscomp):
        self.poscomp = poscomp

    def execute(self):
        x = self.poscomp.y
        z = x-1
        self.poscomp.set_pos_y(z)

    def undo(self) -> None:
        from command.downCommand import downCommand
        Invoker(downCommand()).invoke()