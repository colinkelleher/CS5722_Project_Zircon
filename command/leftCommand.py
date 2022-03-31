from command.Command import Command
from command.Invoker import Invoker



class leftCommand(Command):
    def __init__(self, poscomp):
        self.poscomp = poscomp

    def execute(self):
        x = self.poscomp.x
        y = x-1
        self.poscomp.set_pos_x(y)

    def undo(self) -> None:
        from command.rightCommand import rightCommand
        Invoker(rightCommand()).invoke()

