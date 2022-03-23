from command.Command import Command

class Invoker:
    onStart = None
    onFinish = None

    def setStart(self,command:Command):
        self.onStart = command

    def setFinsih(self, command:Command):
        self.onFinish = command

    def completeTask(self)-> None:

        print("Invoker - task execution")
        if isinstance(self.onStart, Command):
            self.onStart.execute()

        print("Carrying out task...")

        if isinstance(self.onFinish, Command):
            self.onFinish.execute()
