from command.Command import Command
from command.Invoker import Invoker
from command.upCommand import upCommand


class downCommand(Command):
    def __init__(self, poscomp):
        self.poscomp = poscomp

    def execute(self):
        x = self.poscomp.y
        z = x+1
        self.poscomp.set_pos_y(z)

    def undo(self):
        Invoker(upCommand()).invoke()
