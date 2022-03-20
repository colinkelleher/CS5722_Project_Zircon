from unittest import TestCase

from component.Component import Component
from component.PositionComponent import PositionComponent
from entity.Entity import Entity


class TestEntity(TestCase):
    def test_set(self):
        player = Entity()
        poscomp = PositionComponent()
        player.set(poscomp)

        self.assertTrue(PositionComponent in player.components)
        self.assertTrue(player.has(PositionComponent))
        self.assertTrue(player.has(Component))
