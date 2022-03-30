from unittest import TestCase

from component.Component import Component
from component.DisplayComponent import DisplayComponent

class TestDisplayComponent(TestCase):
    def test_set_color(self):
        dispcomp = DisplayComponent("test",(2,2,2),(2,2,2))
        dispcomp.set_fg_color((2,2,2))
        self.assertTrue(dispcomp.fg_color == (2,2,2))
