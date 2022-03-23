from command.Command import Command
from command.Receiver import Receiver


class ConcreteCommand(Command):

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self.receiver = receiver
        self.a = a
        self.b = b

    def execute(self) -> None:
        self.receiver.completeTask1(self.a)
        self.receiver.completeTask2(self.b)
        print("Delegating stuff to be done by a receiver")
