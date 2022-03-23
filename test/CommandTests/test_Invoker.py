from unittest import TestCase
from command.Invoker import Invoker
from command.ConcreteCommand import ConcreteCommand
from command.Receiver import Receiver


class TestInvoker(TestCase):
    def test_set_start(self):
        inv = Invoker()
        rec = Receiver()
        com = ConcreteCommand(rec,"test1","test2")
        inv.setStart(com)
        self.assertTrue(inv.onStart == com)

    def test_set_finish(self):
        inv = Invoker()
        rec = Receiver()
        com = ConcreteCommand(rec,"test1","test2")
        inv.setFinish(com)
        self.assertTrue(inv.onFinish == com)

