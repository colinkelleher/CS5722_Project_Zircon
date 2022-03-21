from unittest import TestCase
from component.Component import Component
from component.WalkableComponent import WalkableComponent


class TestWalkableComponent(TestCase):
    def test_set_walkable(self):
        wkcomp = WalkableComponent(True)
        res = wkcomp.get_walkable()
        self.assertTrue(res== True)
        wkcomp.set_walkable(False)
        res1 = wkcomp.get_walkable()
        self.assertTrue(res1 == False)
