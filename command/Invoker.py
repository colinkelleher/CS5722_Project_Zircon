from command.Command import Command

class Invoker:
    def __init__(self, command:Command):
        self.command = command

    def setCommand(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


