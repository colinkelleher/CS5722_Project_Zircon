from unittest import TestCase
from component.Component import Component
from component.PositionComponent import PositionComponent


class TestPositionComponent(TestCase):

    def test_set_pos(self):
        poscomp = PositionComponent(123,123)
        self.assertTrue(poscomp.x == 123 and poscomp.y == 123)
        poscomp.set_pos(321,321)
        self.assertTrue(poscomp.x == 321 and poscomp.y == 321)

    def test_set_pos_x(self):
        poscomp1 = PositionComponent(123,123)
        self.assertTrue(poscomp1.x == 123 and poscomp1.y == 123)
        poscomp1.set_pos_x((333))
        self.assertTrue(poscomp1.x == 333)

    def test_set_pos_y(self):
        poscomp1 = PositionComponent(123,123)
        self.assertTrue(poscomp1.x == 123 and poscomp1.y == 123)
        poscomp1.set_pos_y((333))
        self.assertTrue(poscomp1.y == 333)
        self.assertFalse(poscomp1.x == 333)