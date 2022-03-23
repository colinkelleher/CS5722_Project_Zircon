from unittest import TestCase

from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Player import Player


class TestPlayer(TestCase):
    def test_set(self):
        player = Player()
        poscomp = PositionComponent()
        player.set_component(poscomp)

        self.assertTrue(PositionComponent in player.components)
        self.assertTrue(DisplayComponent in player.components)