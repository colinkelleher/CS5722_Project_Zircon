from unittest import TestCase
from command.downCommand import downCommand
from component.PositionComponent import PositionComponent
from command.Invoker import Invoker


class TestdownCommand(TestCase):
    def test_execute(self):
        pc = PositionComponent()
        PositionComponent.set_pos(pc,1,1)
        Invoker(downCommand(pc)).invoke()
        x = pc.get_pos_y()
        self.assertTrue(x == 2)
