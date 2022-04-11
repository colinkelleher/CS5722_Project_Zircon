from command.Command import Command

class exitCommand(Command):
    def execute(self) -> None:
       raise SystemExit

    def undo(self) -> None:
        pass