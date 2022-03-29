from command.Command import Command


class leftCommand(Command):
    def __init__(self, poscomp):
        self.poscomp = poscomp

    def execute(self):
        x = self.poscomp.x
        y = x-1
        self.poscomp.set_pos_x(y)
