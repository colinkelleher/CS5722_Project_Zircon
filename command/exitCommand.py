from command.Command import Command

class exitCommand(Command):
    def __init__(self,):
        pass

    def execute(self) -> None:
       raise SystemExit