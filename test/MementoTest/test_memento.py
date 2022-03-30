from unittest import TestCase

from component.DisplayComponent import DisplayComponent
from component.PositionComponent import PositionComponent
from entity.Enemy import Enemy
from memento.Caretaker import Caretaker


class TestMemento(TestCase):
    def test_memento(self):
        dc = DisplayComponent("@", (50, 50, 50), (50, 50, 50))  # initial state of the entities
        pc = PositionComponent(30, 40)

        enemy = Enemy(dc, pc)

        caretaker = Caretaker()
        caretaker.backup()  # saving the first state of the entites
        caretaker.show_history()

        dc.character = "$"
        dc.bg_color = (100, 100, 100)
        dc.fg_color = (100, 100, 100)
        pc.x = 65
        caretaker.backup()  # saving the second state of the entites
        caretaker.show_history()

        dc.character = "^"
        dc.bg_color = (200, 200, 200)  # bringing some change to the current state of the entities
        dc.fg_color = (200, 200, 200)
        self.assertEqual("^", dc.character)
        self.assertEqual((200, 200, 200), dc.bg_color)
        self.assertEqual((200, 200, 200), dc.fg_color)

        caretaker.undo()  # restoring the previous state
        self.assertEqual("$", dc.character)
        self.assertEqual((100, 100, 100), dc.bg_color)
        self.assertEqual((100, 100, 100), dc.fg_color)
        self.assertEqual(65, pc.x)

        caretaker.undo()  # restoring the intial state
        self.assertEqual("@", dc.character)
        self.assertEqual((50, 50, 50), dc.bg_color)
        self.assertEqual((50, 50, 50), dc.fg_color)
        self.assertEqual(30, pc.x)
