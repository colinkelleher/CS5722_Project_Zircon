from unittest import TestCase
from command.rightCommand import rightCommand
from component.PositionComponent import PositionComponent
from command.Invoker import Invoker


class TestrightCommand(TestCase):
    def test_execute(self):
        pc = PositionComponent()
        PositionComponent.set_pos(pc,1,1)
        Invoker(rightCommand(pc)).invoke()
        x = pc.get_pos_x()
        self.assertTrue(x == 2)
