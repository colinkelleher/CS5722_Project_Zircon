from unittest import TestCase

from component.Component import Component
from component.DisplayComponent import DisplayComponent

class TestDisplayComponent(TestCase):
    def test_set_color(self):
        dispcomp = DisplayComponent("Test",(1,1,1))
        dispcomp.set_color((2,2,2))
        self.assertTrue(dispcomp.color == (2,2,2))
