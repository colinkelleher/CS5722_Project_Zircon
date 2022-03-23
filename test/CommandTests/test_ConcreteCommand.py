from unittest import TestCase
from command.ConcreteCommand import ConcreteCommand
from command.Receiver import Receiver


class TestConcreteCommand(TestCase):
    def test_ConcreteCommand(self):
        rec = Receiver()
        cc = ConcreteCommand(rec,"test1","test2")
        self.assertTrue(cc.receiver == rec)
        self.assertTrue(cc.a =="test1")
        self.assertFalse(cc.b=="test1")


