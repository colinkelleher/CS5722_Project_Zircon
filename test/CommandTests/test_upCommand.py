from unittest import TestCase
from command.upCommand import upCommand
from component.PositionComponent import PositionComponent
from command.Invoker import Invoker


class TestupCommand(TestCase):
    def test_execute(self):
        pc = PositionComponent()
        PositionComponent.set_pos(pc,1,1)
        Invoker(upCommand(pc)).invoke()
        x = pc.get_pos_y()
        self.assertTrue(x == 0)
