from unittest import TestCase
from command.leftCommand import leftCommand
from component.PositionComponent import PositionComponent
from command.Invoker import Invoker


class TestleftCommand(TestCase):
    def test_execute(self):
        pc = PositionComponent()
        PositionComponent.set_pos(pc,1,1)
        Invoker(leftCommand(pc)).invoke()
        x = pc.get_pos_x()
        self.assertTrue(x == 0)
