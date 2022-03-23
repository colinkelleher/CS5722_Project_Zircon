from command.Command import Command
from command.Receiver import Receiver

class Invoker:
    _onStart = None
    _onFinish = None

    def setStart(self,command:Command):
        self._onStart = command

    def setFinish(self, command:Command):
        self._onFinish = command

    def completeTask(self)-> None:

        print("Invoker - task execution")
        if isinstance(self._onStart, Command):
            self._onStart.execute()

        print("Carrying out task...")

        if isinstance(self._onFinish, Command):
            self._onFinish.execute()


