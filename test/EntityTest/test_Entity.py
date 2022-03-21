from unittest import TestCase

from component.Component import Component
from component.PositionComponent import PositionComponent
from entity.Entity import Entity


class TestEntity(TestCase):
    def test_set(self):
        entity = Entity()
        poscomp = Component()
        entity.set(poscomp)
        res = entity.get()

        # self.assertTrue(PositionComponent in player.components)
        # self.assertTrue(player.has(PositionComponent))
        self.assertTrue(poscomp in res)